"""Access NLDI and WaterData databases."""
import logging
import sys
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

import async_retriever as ar
import geopandas as gpd
import numpy as np
import pandas as pd
import pygeoogc as ogc
import pygeoogc.utils as ogc_utils
import pygeoutils as geoutils
from pygeoogc import WFS, InvalidInputValue, ServiceUnavailable, ServiceURL, ZeroMatched
from pygeoutils import InvalidInputType
from requests import Response
from shapely.geometry import MultiPolygon, Polygon

from .core import AGRBase
from .exceptions import InvalidInputRange, MissingItems

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(""))
logger.handlers = [handler]
logger.propagate = False
DEF_CRS = "epsg:4326"
ALT_CRS = "epsg:4269"


class PyGeoAPI:
    """Access `PyGeoAPI <https://labs.waterdata.usgs.gov/api/nldi/pygeoapi>`__ service."""

    @staticmethod
    def _get_url(operation: str) -> str:
        """Set the service url."""
        base_url = ServiceURL().restful.pygeoapi
        return f"{base_url}/nldi-{operation}/jobs?response=document"

    @staticmethod
    def _request_body(id_value: Dict[str, Any]) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
        """Return a valid request body."""
        data = {
            "inputs": [
                {"id": f"{i}", "type": "text/plain", "value": v if isinstance(v, list) else f"{v}"}
                for i, v in id_value.items()
            ]
        }
        return {"json": data}

    @staticmethod
    def _get_response(
        url: str, payload: Dict[str, Dict[str, List[Dict[str, Any]]]]
    ) -> gpd.GeoDataFrame:
        """Post the request and return the response as GeoDataFrame."""
        resp = ar.retrieve([url], "json", [payload], "POST")[0]
        try:
            return geoutils.json2geodf(resp["outputs"])
        except KeyError as ex:
            raise ar.ServiceError(resp) from ex

    @staticmethod
    def _check_coords(
        coords: Union[Tuple[float, float], List[Tuple[float, float]]],
        crs: str,
    ) -> Union[Tuple[float, float], List[List[float]]]:
        """Check the coordinates."""
        if isinstance(coords, tuple):
            if len(coords) != 2:
                raise InvalidInputType("coords", "tuple", "(lon, lat)")
            return ogc_utils.match_crs([coords], crs, DEF_CRS)[0]

        if isinstance(coords, list):
            if len(coords) != 2:
                raise InvalidInputType("coords", "list", "[(lon, lat), (lon, lat)]")
            _coords = ogc_utils.match_crs(coords, crs, DEF_CRS)
            return [[_coords[0][0], _coords[1][0]], [_coords[0][1], _coords[1][1]]]

        raise InvalidInputType("coords", "list or tuple")

    def flow_trace(
        self,
        coord: Tuple[float, float],
        crs: str = DEF_CRS,
        raindrop: bool = False,
        direction: str = "down",
    ) -> gpd.GeoDataFrame:
        """Return a GeoDataFrame from the flowtrace service.

        Parameters
        ----------
        coord : tuple
            The coordinate of the point to trace as a tuple,e.g., (lon, lat).
        crs : str
            The coordinate reference system of the coordinates, defaults to EPSG:4326.
        raindrop : bool, optional
            If True, use raindrop-based flowpaths, i.e. use raindrop trace web service
            with direction set to "none", defaults to False.
        direction : str, optional
            The direction of flowpaths, either "down", "up", or "none". Defaults to "down".

        Returns
        -------
        geopandas.GeoDataFrame
            A GeoDataFrame containing the traced flowline.

        Examples
        --------
        >>> from pynhd import PyGeoAPI
        >>> pygeoapi = PyGeoAPI()
        >>> gdf = pygeoapi.flow_trace(
        ...     (1774209.63, 856381.68), crs="ESRI:102003", raindrop=False, direction="none"
        ... )
        >>> print(gdf.comid.iloc[0])
        22294818
        """
        _coord = self._check_coords(coord, crs)
        url = self._get_url("flowtrace")
        if raindrop:
            direction = "none"
        payload = self._request_body(
            {"lat": _coord[1], "lon": _coord[0], "raindroptrace": raindrop, "direction": direction}
        )
        return self._get_response(url, payload)

    def split_catchment(
        self, coord: Tuple[float, float], crs: str = DEF_CRS, upstream: bool = False
    ) -> gpd.GeoDataFrame:
        """Return a GeoDataFrame from the splitcatchment service.

        Parameters
        ----------
        coord : tuple
            The coordinate of the point to trace as a tuple,e.g., (lon, lat).
        crs : str, optional
            The coordinate reference system of the coordinates, defaults to EPSG:4326.
        upstream : bool, optional
            If True, return all upstream catchments rather than just the local catchment,
            defaults to False.

        Returns
        -------
        geopandas.GeoDataFrame
            A GeoDataFrame containing the local catchment or the entire upstream catchments.

        Examples
        --------
        >>> from pynhd import PyGeoAPI
        >>> pygeoapi = PyGeoAPI()
        >>> gdf = pygeoapi.split_catchment((-73.82705, 43.29139), crs=DEF_CRS, upstream=False)
        >>> print(gdf.catchmentID.iloc[0])
        22294818
        """
        _coord = self._check_coords(coord, crs)
        url = self._get_url("splitcatchment")
        payload = self._request_body({"lat": _coord[1], "lon": _coord[0], "upstream": upstream})
        return self._get_response(url, payload)

    def elevation_profile(
        self,
        coords: List[Tuple[float, float]],
        numpts: int,
        dem_res: int,
        crs: str = DEF_CRS,
    ) -> gpd.GeoDataFrame:
        """Return a GeoDataFrame from the xsatendpts service.

        Parameters
        ----------
        coords : list
            A list of two coordinates to trace as a list of tuples,e.g., [(lon, lat), (lon, lat)].
        numpts : int
            The number of points to extract the elevation profile from the DEM.
        dem_res : int
            The target resolution for requesting the DEM from 3DEP service.
        crs : str, optional
            The coordinate reference system of the coordinates, defaults to EPSG:4326.

        Returns
        -------
        geopandas.GeoDataFrame
            A GeoDataFrame containing the elevation profile along the requested endpoints.

        Examples
        --------
        >>> from pynhd import PyGeoAPI
        >>> pygeoapi = PyGeoAPI()
        >>> gdf = pygeoapi.elevation_profile(
        ...     [(-103.801086, 40.26772), (-103.80097, 40.270568)], numpts=101, dem_res=1, crs=DEF_CRS
        ... )
        >>> print(gdf.iloc[-1, 1])
        411.5906
        """
        _coords = self._check_coords(coords, crs)
        url = self._get_url("xsatendpts")
        payload = self._request_body(
            {"lat": _coords[1], "lon": _coords[0], "numpts": numpts, "3dep_res": dem_res}
        )
        return self._get_response(url, payload)

    def cross_section(
        self, coord: Tuple[float, float], width: float, numpts: int, crs: str = DEF_CRS
    ) -> gpd.GeoDataFrame:
        """Return a GeoDataFrame from the xsatpoint service.

        Parameters
        ----------
        coord : tuple
            The coordinate of the point to extract the cross-section as a tuple,e.g., (lon, lat).
        width : float
            The width of the cross-section in meters.
        numpts : int
            The number of points to extract the cross-section from the DEM.
        crs : str, optional
            The coordinate reference system of the coordinates, defaults to EPSG:4326.

        Returns
        -------
        geopandas.GeoDataFrame
            A GeoDataFrame containing the cross-section at the requested point.

        Examples
        --------
        >>> from pynhd import PyGeoAPI
        >>> pygeoapi = PyGeoAPI()
        >>> gdf = pygeoapi.cross_section((-103.80119, 40.2684), width=1000.0, numpts=101, crs=DEF_CRS)
        >>> print(gdf.iloc[-1, 1])
        1000.0
        """
        _coord = self._check_coords(coord, crs)
        url = self._get_url("xsatpoint")
        payload = self._request_body(
            {"lat": _coord[1], "lon": _coord[0], "width": width, "numpts": numpts}
        )
        return self._get_response(url, payload)


class WaterData:
    """Access to `Water Data <https://labs.waterdata.usgs.gov/geoserver>`__ service.

    Parameters
    ----------
    layer : str
        A valid layer from the WaterData service. Valid layers are:
        ``nhdarea``, ``nhdwaterbody``, ``catchmentsp``, ``nhdflowline_network``
        ``gagesii``, ``huc08``, ``huc12``, ``huc12agg``, and ``huc12all``. Note that
        the layers' worksapce for the Water Data service is ``wmadata`` which will
        be added to the given ``layer`` argument if it is not provided.
    crs : str, optional
        The target spatial reference system, defaults to ``epsg:4326``.
    """

    def __init__(
        self,
        layer: str,
        crs: str = DEF_CRS,
    ) -> None:
        self.layer = layer if ":" in layer else f"wmadata:{layer}"
        self.crs = crs
        self.wfs = WFS(
            ServiceURL().wfs.waterdata,
            layer=self.layer,
            outformat="application/json",
            version="2.0.0",
            crs=ALT_CRS,
        )

    def __repr__(self) -> str:
        """Print the services properties."""
        return (
            "Connected to the WaterData web service on GeoServer:\n"
            + f"URL: {self.wfs.url}\n"
            + f"Version: {self.wfs.version}\n"
            + f"Layer: {self.layer}\n"
            + f"Output Format: {self.wfs.outformat}\n"
            + f"Output CRS: {self.crs}"
        )

    def bybox(
        self, bbox: Tuple[float, float, float, float], box_crs: str = DEF_CRS
    ) -> gpd.GeoDataFrame:
        """Get features within a bounding box."""
        resp = self.wfs.getfeature_bybox(bbox, box_crs, always_xy=True)
        return self._to_geodf(resp)

    def bygeom(
        self,
        geometry: Union[Polygon, MultiPolygon],
        geo_crs: str = DEF_CRS,
        xy: bool = True,
        predicate: str = "INTERSECTS",
    ) -> gpd.GeoDataFrame:
        """Get features within a geometry.

        Parameters
        ----------
        geometry : shapely.geometry
            The input geometry
        geo_crs : str, optional
            The CRS of the input geometry, default to epsg:4326.
        xy : bool, optional
            Whether axis order of the input geometry is xy or yx.
        predicate : str, optional
            The geometric prediacte to use for requesting the data, defaults to
            INTERSECTS. Valid predicates are:
            ``EQUALS``, ``DISJOINT``, ``INTERSECTS``, ``TOUCHES``, ``CROSSES``, ``WITHIN``
            ``CONTAINS``, ``OVERLAPS``, ``RELATE``, ``BEYOND``

        Returns
        -------
        geopandas.GeoDataFrame
            The requested features in the given geometry.
        """
        resp = self.wfs.getfeature_bygeom(geometry, geo_crs, always_xy=not xy, predicate=predicate)
        return self._to_geodf(resp)

    def bydistance(
        self, coords: Tuple[float, float], distance: int, loc_crs: str = DEF_CRS
    ) -> gpd.GeoDataFrame:
        """Get features within a radius (in meters) of a point."""
        if not (isinstance(coords, tuple) and len(coords) == 2):
            raise InvalidInputType("coods", "tuple of length 2", "(x, y)")

        x, y = ogc.utils.match_crs([coords], loc_crs, ALT_CRS)[0]
        cql_filter = f"DWITHIN(the_geom,POINT({y:.6f} {x:.6f}),{distance},meters)"
        resp = self.wfs.getfeature_byfilter(cql_filter, "GET")
        return self._to_geodf(resp)

    def byid(self, featurename: str, featureids: Union[List[str], str]) -> gpd.GeoDataFrame:
        """Get features based on IDs."""
        resp = self.wfs.getfeature_byid(featurename, featureids)
        return self._to_geodf(resp)

    def byfilter(self, cql_filter: str, method: str = "GET") -> gpd.GeoDataFrame:
        """Get features based on a CQL filter."""
        resp = self.wfs.getfeature_byfilter(cql_filter, method)
        return self._to_geodf(resp)

    def _to_geodf(self, resp: Response) -> gpd.GeoDataFrame:
        """Convert a response from WaterData to a GeoDataFrame.

        Parameters
        ----------
        resp : Response
            A response from a WaterData request.

        Returns
        -------
        geopandas.GeoDataFrame
            The requested features in a GeoDataFrames.
        """
        return geoutils.json2geodf(resp, ALT_CRS, self.crs)


class NHDPlusHR(AGRBase):
    """Access NHDPlus HR database through the National Map ArcGISRESTful.

    Parameters
    ----------
    layer : str, optional
        A valid service layer. To see a list of available layers instantiate the class
        without passing any argument like so ``NHDPlusHR()``.
    outfields : str or list, optional
        Target field name(s), default to "*" i.e., all the fields.
    crs : str, optional
        Target spatial reference, default to EPSG:4326
    service : str, optional
        Name of the web service to use, defaults to hydro. Supported web services are:

        * hydro: https://hydro.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/MapServer
        * edits: https://edits.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/NHDPlus_HR/MapServer

    auto_switch : bool, optional
        Automatically switch to other services' URL if the first one doesn't work, default to False.
    """

    def __init__(
        self,
        layer: Optional[str] = None,
        outfields: Union[str, List[str]] = "*",
        crs: str = DEF_CRS,
        service: str = "hydro",
        auto_switch: bool = False,
    ):
        super().__init__(layer, outfields, crs)
        service_list = {
            "hydro": ServiceURL().restful.nhdplushr,
            "edits": ServiceURL().restful.nhdplushr_edits,
        }
        if layer is None:
            raise InvalidInputValue("layer", list(self.get_validlayers(service_list[service])))
        self.connect_to(service, service_list, auto_switch)


class NLDI:
    """Access the Hydro Network-Linked Data Index (NLDI) service."""

    def __init__(self) -> None:
        self.base_url = ServiceURL().restful.nldi

        resp = ar.retrieve(["/".join([self.base_url, "linked-data"])], "json")[0]
        self.valid_fsources = {r["source"]: r["sourceName"] for r in resp}

        resp = ar.retrieve(["/".join([self.base_url, "lookups"])], "json")[0]
        self.valid_chartypes = {r["type"]: r["typeName"] for r in resp}

    @staticmethod
    def _missing_warning(n_miss: int, n_tot: int) -> None:
        """Show a warning if there are missing features."""
        logger.warning(
            " ".join(
                [
                    f"{n_miss} of {n_tot} inputs didn't return any features.",
                    "They are returned as a list.",
                ]
            )
        )

    def getfeature_byid(
        self, fsource: str, fid: Union[str, List[str]]
    ) -> Union[gpd.GeoDataFrame, Tuple[gpd.GeoDataFrame, List[str]]]:
        """Get feature(s) based ID(s).

        Parameters
        ----------
        fsource : str
            The name of feature(s) source. The valid sources are:
            comid, huc12pp, nwissite, wade, wqp
        fid : str or list
            Feature ID(s).

        Returns
        -------
        geopandas.GeoDataFrame or (geopandas.GeoDataFrame, list)
            NLDI indexed features in EPSG:4326. If some IDs don't return any features
            a list of missing ID(s) are returned as well.
        """
        self._validate_fsource(fsource)
        fid = fid if isinstance(fid, list) else [fid]
        urls = {f: ("/".join([self.base_url, "linked-data", fsource, f]), None) for f in fid}
        features, not_found = self._get_urls(urls)

        if len(not_found) > 0:
            self._missing_warning(len(not_found), len(fid))
            return features, not_found

        return features

    def comid_byloc(
        self,
        coords: Union[Tuple[float, float], List[Tuple[float, float]]],
        loc_crs: str = DEF_CRS,
    ) -> Union[gpd.GeoDataFrame, Tuple[gpd.GeoDataFrame, List[Tuple[float, float]]]]:
        """Get the closest ComID(s) based on coordinates.

        Parameters
        ----------
        coords : tuple or list
            A tuple of length two (x, y) or a list of them.
        loc_crs : str, optional
            The spatial reference of the input coordinate, defaults to EPSG:4326.

        Returns
        -------
        geopandas.GeoDataFrame or (geopandas.GeoDataFrame, list)
            NLDI indexed ComID(s) in EPSG:4326. If some coords don't return any ComID
            a list of missing coords are returned as well.
        """
        _coords = [coords] if isinstance(coords, tuple) else coords

        if not isinstance(_coords, list) or any(len(c) != 2 for c in _coords):
            raise InvalidInputType("coords", "list or tuple")

        _coords = ogc.utils.match_crs(_coords, loc_crs, DEF_CRS)

        base_url = "/".join([self.base_url, "linked-data", "comid", "position"])
        urls = {
            f"{(lon, lat)}": (base_url, {"coords": f"POINT({lon} {lat})"}) for lon, lat in _coords
        }
        comids, not_found = self._get_urls(urls)

        if len(comids) == 0:
            raise ZeroMatched

        comids = comids.reset_index(drop=True)

        if len(not_found) > 0:
            self._missing_warning(len(not_found), len(_coords))
            return comids, not_found

        return comids

    def get_basins(
        self,
        station_ids: Union[str, List[str]],
        split_catchment: bool = False,
    ) -> Union[gpd.GeoDataFrame, Tuple[gpd.GeoDataFrame, List[str]]]:
        """Get basins for a list of station IDs.

        Parameters
        ----------
        station_ids : str or list
            USGS station ID(s).
        split_catchment : bool, optional
            If True, split the basin at the watershed outlet location. Default to False.

        Returns
        -------
        geopandas.GeoDataFrame or (geopandas.GeoDataFrame, list)
            NLDI indexed basins in EPSG:4326. If some IDs don't return any features
            a list of missing ID(s) are returned as well.
        """
        station_ids = station_ids if isinstance(station_ids, list) else [station_ids]
        payload = {"splitCatchment": "true"} if split_catchment else None
        urls = {
            s: (f"{self.base_url}/linked-data/nwissite/USGS-{s}/basin", payload)
            for s in station_ids
        }
        basins, not_found = self._get_urls(urls)
        basins = basins.reset_index(level=1, drop=True)
        basins.index.rename("identifier", inplace=True)

        if len(not_found) > 0:
            self._missing_warning(len(not_found), len(station_ids))
            return basins, not_found

        return basins

    def getcharacteristic_byid(
        self,
        comids: Union[List[str], str],
        char_type: str,
        char_ids: Union[str, List[str]] = "all",
        values_only: bool = True,
    ) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
        """Get characteristics using a list ComIDs.

        Parameters
        ----------
        comids : str or list
            The ID of the feature.
        char_type : str
            Type of the characteristic. Valid values are ``local`` for
            individual reach catchments, ``tot`` for network-accumulated values
            using total cumulative drainage area and ``div`` for network-accumulated values
            using divergence-routed.
        char_ids : str or list, optional
            Name(s) of the target characteristics, default to all.
        values_only : bool, optional
            Whether to return only ``characteristic_value`` as a series, default to True.
            If is set to False, ``percent_nodata`` is returned as well.

        Returns
        -------
        pandas.DataFrame or tuple of pandas.DataFrame
            Either only ``characteristic_value`` as a dataframe or
            or if ``values_only`` is Fale return ``percent_nodata`` as well.
        """
        if char_type not in self.valid_chartypes:
            valids = [f'"{s}" for {d}' for s, d in self.valid_chartypes.items()]
            raise InvalidInputValue("char", valids)

        comids = comids if isinstance(comids, list) else [comids]
        v_dict, nd_dict = {}, {}

        if char_ids == "all":
            payload = None
        else:
            _char_ids = char_ids if isinstance(char_ids, list) else [char_ids]
            valid_charids = self.get_validchars(char_type)

            idx = valid_charids.index
            if any(c not in idx for c in _char_ids):
                vids = valid_charids["characteristic_description"]
                raise InvalidInputValue("char_id", [f'"{s}" for {d}' for s, d in vids.items()])
            payload = {"characteristicId": ",".join(_char_ids)}

        for comid in comids:
            url = "/".join([self.base_url, "linked-data", "comid", f"{comid}", char_type])
            rjson = self._get_url(url, payload)
            char = pd.DataFrame.from_dict(rjson["characteristics"], orient="columns").T
            char.columns = char.iloc[0]
            char = char.drop(index="characteristic_id")

            v_dict[comid] = char.loc["characteristic_value"]
            if values_only:
                continue

            nd_dict[comid] = char.loc["percent_nodata"]

        def todf(df_dict: Dict[str, pd.DataFrame]) -> pd.DataFrame:
            df = pd.DataFrame.from_dict(df_dict, orient="index")
            df[df == ""] = np.nan
            df.index = df.index.astype("int64")
            return df.astype("f4")

        chars = todf(v_dict)
        if values_only:
            return chars

        return chars, todf(nd_dict)

    def get_validchars(self, char_type: str) -> pd.DataFrame:
        """Get all the available characteristics IDs for a given characteristics type."""
        resp = ar.retrieve(
            ["/".join([self.base_url, "lookups", char_type, "characteristics"])], "json"
        )
        c_list = ogc.utils.traverse_json(resp[0], ["characteristicMetadata", "characteristic"])
        return pd.DataFrame.from_dict(
            {c.pop("characteristic_id"): c for c in c_list}, orient="index"
        )

    def navigate_byid(
        self,
        fsource: str,
        fid: str,
        navigation: str,
        source: str,
        distance: int = 500,
    ) -> gpd.GeoDataFrame:
        """Navigate the NHDPlus database from a single feature id up to a distance.

        Parameters
        ----------
        fsource : str
            The name of feature source. The valid sources are:
            ``comid``, ``huc12pp``, ``nwissite``, ``wade``, ``WQP``.
        fid : str
            The ID of the feature.
        navigation : str
            The navigation method.
        source : str, optional
            Return the data from another source after navigating
            the features using fsource, defaults to None.
        distance : int, optional
            Limit the search for navigation up to a distance in km,
            defaults is 500 km. Note that this is an expensive request so you
            have be mindful of the value that you provide. The value must be
            between 1 to 9999 km.

        Returns
        -------
        geopandas.GeoDataFrame
            NLDI indexed features in EPSG:4326.
        """
        if not (1 <= distance <= 9999):
            raise InvalidInputRange("distance", "[1, 9999]")

        self._validate_fsource(fsource)

        url = "/".join([self.base_url, "linked-data", fsource, fid, "navigation"])

        valid_navigations = self._get_url(url)
        if navigation not in valid_navigations.keys():
            raise InvalidInputValue("navigation", list(valid_navigations.keys()))

        url = valid_navigations[navigation]

        r_json = self._get_url(url)
        valid_sources = {s["source"].lower(): s["features"] for s in r_json}  # type: ignore
        if source not in valid_sources:
            raise InvalidInputValue("source", list(valid_sources.keys()))

        url = valid_sources[source]
        payload = {"distance": f"{int(distance)}"}

        return geoutils.json2geodf(self._get_url(url, payload), ALT_CRS, DEF_CRS)

    def navigate_byloc(
        self,
        coords: Tuple[float, float],
        navigation: Optional[str] = None,
        source: Optional[str] = None,
        loc_crs: str = DEF_CRS,
        distance: int = 500,
    ) -> gpd.GeoDataFrame:
        """Navigate the NHDPlus database from a coordinate.

        Parameters
        ----------
        coords : tuple
            A tuple of length two (x, y).
        navigation : str, optional
            The navigation method, defaults to None which throws an exception
            if comid_only is False.
        source : str, optional
            Return the data from another source after navigating
            the features using fsource, defaults to None which throws an exception
            if comid_only is False.
        loc_crs : str, optional
            The spatial reference of the input coordinate, defaults to EPSG:4326.
        distance : int, optional
            Limit the search for navigation up to a distance in km,
            defaults to 500 km. Note that this is an expensive request so you
            have be mindful of the value that you provide. If you want to get
            all the available features you can pass a large distance like 9999999.

        Returns
        -------
        geopandas.GeoDataFrame
            NLDI indexed features in EPSG:4326.
        """
        if not (isinstance(coords, tuple) and len(coords) == 2):
            raise InvalidInputType("coods", "tuple of length 2", "(x, y)")
        resp = self.comid_byloc(coords, loc_crs)
        comid_df = resp[0] if isinstance(resp, tuple) else resp
        comid = comid_df.comid.iloc[0]

        if navigation is None or source is None:
            raise MissingItems(["navigation", "source"])

        return self.navigate_byid("comid", comid, navigation, source, distance)

    def _validate_fsource(self, fsource: str) -> None:
        """Check if the given feature source is valid."""
        if fsource not in self.valid_fsources:
            valids = [f'"{s}" for {d}' for s, d in self.valid_fsources.items()]
            raise InvalidInputValue("fsource", valids)

    def _get_urls(
        self, urls: Mapping[Any, Tuple[str, Optional[Dict[str, str]]]]
    ) -> Tuple[gpd.GeoDataFrame, List[str]]:
        """Get basins for a list of station IDs.

        Parameters
        ----------
        urls : dict
            A dict with keys as feature ids and values as corresponding url and payload.

        Returns
        -------
        (geopandas.GeoDataFrame, list)
            NLDI indexed features in EPSG:4326 and list of ID(s) that no feature was found.
        """
        not_found = []
        resp = []
        for f, (u, p) in urls.items():
            try:
                rjson = self._get_url(u, p)
                resp.append((f, geoutils.json2geodf(rjson, ALT_CRS, DEF_CRS)))
            except (ZeroMatched, InvalidInputType, ar.ServiceError):
                not_found.append(f)

        if len(resp) == 0:
            raise ZeroMatched

        resp_df = gpd.GeoDataFrame(pd.concat(dict(resp)))

        return resp_df, not_found

    def _get_url(self, url: str, payload: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Send a request to the service using GET method."""
        if payload is None:
            payload = {"f": "json"}
        else:
            payload.update({"f": "json"})

        try:
            return ar.retrieve([url], "json", [{"params": payload}])[0]
        except ar.ServiceError as ex:
            raise ZeroMatched from ex
        except ConnectionError as ex:
            raise ServiceUnavailable(self.base_url) from ex
