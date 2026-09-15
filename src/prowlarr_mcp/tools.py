"""Generated from the OpenAPI document. Do not edit by hand.

Regenerate with:

    python scripts/generate_tools.py openapi.json src/prowlarr_mcp/tools.py

One tool per operation, 128 of them, covering the whole API.
"""

from .runtime import _DESTRUCTIVE, _READ, _WRITE, call, mcp


@mcp.tool(annotations=_WRITE)
def create_applications(body: dict, force_save: bool | None = None) -> str:
    """Create Application.

    POST /api/v1/applications

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v1/applications", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_applications_action_by_name(name: str, body: dict) -> str:
    """Create Application.

    POST /api/v1/applications/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/applications/action/{name}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_applications_test(body: dict, force_test: bool | None = None) -> str:
    """Create Application.

    POST /api/v1/applications/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v1/applications/test", query={"forceTest": force_test}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_applications_testall() -> str:
    """Create Application.

    POST /api/v1/applications/testall
    """
    return call("POST", "/api/v1/applications/testall", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_appprofile(body: dict) -> str:
    """Create AppProfile.

    POST /api/v1/appprofile

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/appprofile", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_command(body: dict) -> str:
    """Create Command.

    POST /api/v1/command

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/command", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_customfilter(body: dict) -> str:
    """Create CustomFilter.

    POST /api/v1/customfilter

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/customfilter", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_downloadclient(body: dict, force_save: bool | None = None) -> str:
    """Create DownloadClient.

    POST /api/v1/downloadclient

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v1/downloadclient", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_downloadclient_action_by_name(name: str, body: dict) -> str:
    """Create DownloadClient.

    POST /api/v1/downloadclient/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/downloadclient/action/{name}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_downloadclient_test(body: dict, force_test: bool | None = None) -> str:
    """Create DownloadClient.

    POST /api/v1/downloadclient/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v1/downloadclient/test", query={"forceTest": force_test}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_downloadclient_testall() -> str:
    """Create DownloadClient.

    POST /api/v1/downloadclient/testall
    """
    return call("POST", "/api/v1/downloadclient/testall", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_indexer(body: dict, force_save: bool | None = None) -> str:
    """Create Indexer.

    POST /api/v1/indexer

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v1/indexer", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_indexer_action_by_name(name: str, body: dict) -> str:
    """Create Indexer.

    POST /api/v1/indexer/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/indexer/action/{name}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_indexer_test(body: dict, force_test: bool | None = None) -> str:
    """Create Indexer.

    POST /api/v1/indexer/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v1/indexer/test", query={"forceTest": force_test}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_indexer_testall() -> str:
    """Create Indexer.

    POST /api/v1/indexer/testall
    """
    return call("POST", "/api/v1/indexer/testall", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_indexerproxy(body: dict, force_save: bool | None = None) -> str:
    """Create IndexerProxy.

    POST /api/v1/indexerproxy

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v1/indexerproxy", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_indexerproxy_action_by_name(name: str, body: dict) -> str:
    """Create IndexerProxy.

    POST /api/v1/indexerproxy/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/indexerproxy/action/{name}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_indexerproxy_test(body: dict, force_test: bool | None = None) -> str:
    """Create IndexerProxy.

    POST /api/v1/indexerproxy/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v1/indexerproxy/test", query={"forceTest": force_test}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_indexerproxy_testall() -> str:
    """Create IndexerProxy.

    POST /api/v1/indexerproxy/testall
    """
    return call("POST", "/api/v1/indexerproxy/testall", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_login(body: dict, return_url: str | None = None) -> str:
    """Create Authentication.

    POST /login

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        return_url: Query parameter.
    """
    return call("POST", "/login", query={"returnUrl": return_url}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_notification(body: dict, force_save: bool | None = None) -> str:
    """Create Notification.

    POST /api/v1/notification

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v1/notification", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_notification_action_by_name(name: str, body: dict) -> str:
    """Create Notification.

    POST /api/v1/notification/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/notification/action/{name}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_notification_test(body: dict, force_test: bool | None = None) -> str:
    """Create Notification.

    POST /api/v1/notification/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v1/notification/test", query={"forceTest": force_test}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_notification_testall() -> str:
    """Create Notification.

    POST /api/v1/notification/testall
    """
    return call("POST", "/api/v1/notification/testall", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_search(body: dict) -> str:
    """Create Search.

    POST /api/v1/search

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/search", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_search_bulk(body: dict) -> str:
    """Create Search.

    POST /api/v1/search/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/search/bulk", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_system_backup_restore_by_id(id_: int) -> str:
    """Create Backup.

    POST /api/v1/system/backup/restore/{id}

    Args:
        id_: Path parameter.
    """
    return call("POST", f"/api/v1/system/backup/restore/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_system_backup_restore_upload() -> str:
    """Create Backup.

    POST /api/v1/system/backup/restore/upload
    """
    return call("POST", "/api/v1/system/backup/restore/upload", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_system_restart() -> str:
    """Create System.

    POST /api/v1/system/restart
    """
    return call("POST", "/api/v1/system/restart", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_system_shutdown() -> str:
    """Create System.

    POST /api/v1/system/shutdown
    """
    return call("POST", "/api/v1/system/shutdown", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def create_tag(body: dict) -> str:
    """Create Tag.

    POST /api/v1/tag

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/tag", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_applications_bulk(body: dict) -> str:
    """Delete Application.

    DELETE /api/v1/applications/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v1/applications/bulk", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_applications_by_id(id_: int) -> str:
    """Delete Application.

    DELETE /api/v1/applications/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/applications/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_appprofile_by_id(id_: int) -> str:
    """Delete AppProfile.

    DELETE /api/v1/appprofile/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/appprofile/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_command_by_id(id_: int) -> str:
    """Delete Command.

    DELETE /api/v1/command/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/command/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_customfilter_by_id(id_: int) -> str:
    """Delete CustomFilter.

    DELETE /api/v1/customfilter/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/customfilter/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_downloadclient_bulk(body: dict) -> str:
    """Delete DownloadClient.

    DELETE /api/v1/downloadclient/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v1/downloadclient/bulk", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_downloadclient_by_id(id_: int) -> str:
    """Delete DownloadClient.

    DELETE /api/v1/downloadclient/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/downloadclient/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_indexer_bulk(body: dict) -> str:
    """Delete Indexer.

    DELETE /api/v1/indexer/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v1/indexer/bulk", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_indexer_by_id(id_: int) -> str:
    """Delete Indexer.

    DELETE /api/v1/indexer/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/indexer/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_indexerproxy_by_id(id_: int) -> str:
    """Delete IndexerProxy.

    DELETE /api/v1/indexerproxy/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/indexerproxy/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_notification_by_id(id_: int) -> str:
    """Delete Notification.

    DELETE /api/v1/notification/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/notification/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_system_backup_by_id(id_: int) -> str:
    """Delete Backup.

    DELETE /api/v1/system/backup/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/system/backup/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_tag_by_id(id_: int) -> str:
    """Delete Tag.

    DELETE /api/v1/tag/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v1/tag/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_applications_by_id(id_: int) -> str:
    """Read Application.

    GET /api/v1/applications/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/applications/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_appprofile_by_id(id_: int) -> str:
    """Read AppProfile.

    GET /api/v1/appprofile/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/appprofile/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_by_id_api(id_: int, t: str | None = None, q: str | None = None, cat: str | None = None, imdbid: str | None = None, tmdbid: int | None = None, extended: str | None = None, limit: int | None = None, offset: int | None = None, minage: int | None = None, maxage: int | None = None, minsize: int | None = None, maxsize: int | None = None, rid: int | None = None, tvmazeid: int | None = None, traktid: int | None = None, tvdbid: int | None = None, doubanid: int | None = None, season: int | None = None, ep: str | None = None, album: str | None = None, artist: str | None = None, label: str | None = None, track: str | None = None, year: int | None = None, genre: str | None = None, author: str | None = None, title: str | None = None, publisher: str | None = None, configured: str | None = None, source: str | None = None, host: str | None = None, server: str | None = None) -> str:
    """Read Newznab.

    GET /{id}/api

    Args:
        id_: Path parameter.
        t: Query parameter.
        q: Query parameter.
        cat: Query parameter.
        imdbid: Query parameter.
        tmdbid: Query parameter.
        extended: Query parameter.
        limit: Query parameter.
        offset: Query parameter.
        minage: Query parameter.
        maxage: Query parameter.
        minsize: Query parameter.
        maxsize: Query parameter.
        rid: Query parameter.
        tvmazeid: Query parameter.
        traktid: Query parameter.
        tvdbid: Query parameter.
        doubanid: Query parameter.
        season: Query parameter.
        ep: Query parameter.
        album: Query parameter.
        artist: Query parameter.
        label: Query parameter.
        track: Query parameter.
        year: Query parameter.
        genre: Query parameter.
        author: Query parameter.
        title: Query parameter.
        publisher: Query parameter.
        configured: Query parameter.
        source: Query parameter.
        host: Query parameter.
        server: Query parameter.
    """
    return call("GET", f"/{id_}/api", query={"t": t, "q": q, "cat": cat, "imdbid": imdbid, "tmdbid": tmdbid, "extended": extended, "limit": limit, "offset": offset, "minage": minage, "maxage": maxage, "minsize": minsize, "maxsize": maxsize, "rid": rid, "tvmazeid": tvmazeid, "traktid": traktid, "tvdbid": tvdbid, "doubanid": doubanid, "season": season, "ep": ep, "album": album, "artist": artist, "label": label, "track": track, "year": year, "genre": genre, "author": author, "title": title, "publisher": publisher, "configured": configured, "source": source, "host": host, "server": server}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_by_id_download(id_: int, link: str | None = None, file: str | None = None) -> str:
    """Read Newznab.

    GET /{id}/download

    Args:
        id_: Path parameter.
        link: Query parameter.
        file: Query parameter.
    """
    return call("GET", f"/{id_}/download", query={"link": link, "file": file}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_by_path(path: str) -> str:
    """Read StaticResource.

    GET /{path}

    Args:
        path: Path parameter.
    """
    return call("GET", f"/{path}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_command_by_id(id_: int) -> str:
    """Read Command.

    GET /api/v1/command/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/command/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_config_development_by_id(id_: int) -> str:
    """Read DevelopmentConfig.

    GET /api/v1/config/development/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/config/development/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_config_downloadclient_by_id(id_: int) -> str:
    """Read DownloadClientConfig.

    GET /api/v1/config/downloadclient/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/config/downloadclient/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_config_host_by_id(id_: int) -> str:
    """Read HostConfig.

    GET /api/v1/config/host/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/config/host/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_config_ui_by_id(id_: int) -> str:
    """Read UiConfig.

    GET /api/v1/config/ui/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/config/ui/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_content_by_path(path: str) -> str:
    """Read StaticResource.

    GET /content/{path}

    Args:
        path: Path parameter.
    """
    return call("GET", f"/content/{path}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_customfilter_by_id(id_: int) -> str:
    """Read CustomFilter.

    GET /api/v1/customfilter/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/customfilter/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_downloadclient_by_id(id_: int) -> str:
    """Read DownloadClient.

    GET /api/v1/downloadclient/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/downloadclient/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_indexer_by_id(id_: int) -> str:
    """Read Indexer.

    GET /api/v1/indexer/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/indexer/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_indexer_by_id_download(id_: int, link: str | None = None, file: str | None = None) -> str:
    """Read Newznab.

    GET /api/v1/indexer/{id}/download

    Args:
        id_: Path parameter.
        link: Query parameter.
        file: Query parameter.
    """
    return call("GET", f"/api/v1/indexer/{id_}/download", query={"link": link, "file": file}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_indexer_by_id_newznab(id_: int, t: str | None = None, q: str | None = None, cat: str | None = None, imdbid: str | None = None, tmdbid: int | None = None, extended: str | None = None, limit: int | None = None, offset: int | None = None, minage: int | None = None, maxage: int | None = None, minsize: int | None = None, maxsize: int | None = None, rid: int | None = None, tvmazeid: int | None = None, traktid: int | None = None, tvdbid: int | None = None, doubanid: int | None = None, season: int | None = None, ep: str | None = None, album: str | None = None, artist: str | None = None, label: str | None = None, track: str | None = None, year: int | None = None, genre: str | None = None, author: str | None = None, title: str | None = None, publisher: str | None = None, configured: str | None = None, source: str | None = None, host: str | None = None, server: str | None = None) -> str:
    """Read Newznab.

    GET /api/v1/indexer/{id}/newznab

    Args:
        id_: Path parameter.
        t: Query parameter.
        q: Query parameter.
        cat: Query parameter.
        imdbid: Query parameter.
        tmdbid: Query parameter.
        extended: Query parameter.
        limit: Query parameter.
        offset: Query parameter.
        minage: Query parameter.
        maxage: Query parameter.
        minsize: Query parameter.
        maxsize: Query parameter.
        rid: Query parameter.
        tvmazeid: Query parameter.
        traktid: Query parameter.
        tvdbid: Query parameter.
        doubanid: Query parameter.
        season: Query parameter.
        ep: Query parameter.
        album: Query parameter.
        artist: Query parameter.
        label: Query parameter.
        track: Query parameter.
        year: Query parameter.
        genre: Query parameter.
        author: Query parameter.
        title: Query parameter.
        publisher: Query parameter.
        configured: Query parameter.
        source: Query parameter.
        host: Query parameter.
        server: Query parameter.
    """
    return call("GET", f"/api/v1/indexer/{id_}/newznab", query={"t": t, "q": q, "cat": cat, "imdbid": imdbid, "tmdbid": tmdbid, "extended": extended, "limit": limit, "offset": offset, "minage": minage, "maxage": maxage, "minsize": minsize, "maxsize": maxsize, "rid": rid, "tvmazeid": tvmazeid, "traktid": traktid, "tvdbid": tvdbid, "doubanid": doubanid, "season": season, "ep": ep, "album": album, "artist": artist, "label": label, "track": track, "year": year, "genre": genre, "author": author, "title": title, "publisher": publisher, "configured": configured, "source": source, "host": host, "server": server}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_indexerproxy_by_id(id_: int) -> str:
    """Read IndexerProxy.

    GET /api/v1/indexerproxy/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/indexerproxy/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_log_file_by_filename(filename: str) -> str:
    """Read LogFile.

    GET /api/v1/log/file/{filename}

    Args:
        filename: Path parameter.
    """
    return call("GET", f"/api/v1/log/file/{filename}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_log_file_update_by_filename(filename: str) -> str:
    """Read UpdateLogFile.

    GET /api/v1/log/file/update/{filename}

    Args:
        filename: Path parameter.
    """
    return call("GET", f"/api/v1/log/file/update/{filename}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_notification_by_id(id_: int) -> str:
    """Read Notification.

    GET /api/v1/notification/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/notification/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_system_task_by_id(id_: int) -> str:
    """Read Task.

    GET /api/v1/system/task/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/system/task/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_tag_by_id(id_: int) -> str:
    """Read Tag.

    GET /api/v1/tag/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/tag/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_tag_detail_by_id(id_: int) -> str:
    """Read TagDetails.

    GET /api/v1/tag/detail/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v1/tag/detail/{id_}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_api() -> str:
    """Read ApiInfo.

    GET /api
    """
    return call("GET", "/api", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_applications() -> str:
    """Read Application.

    GET /api/v1/applications
    """
    return call("GET", "/api/v1/applications", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_applications_schema() -> str:
    """Read Application.

    GET /api/v1/applications/schema
    """
    return call("GET", "/api/v1/applications/schema", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_appprofile() -> str:
    """Read AppProfile.

    GET /api/v1/appprofile
    """
    return call("GET", "/api/v1/appprofile", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_appprofile_schema() -> str:
    """Read AppProfile.

    GET /api/v1/appprofile/schema
    """
    return call("GET", "/api/v1/appprofile/schema", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_command() -> str:
    """Read Command.

    GET /api/v1/command
    """
    return call("GET", "/api/v1/command", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_config_development() -> str:
    """Read DevelopmentConfig.

    GET /api/v1/config/development
    """
    return call("GET", "/api/v1/config/development", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_config_downloadclient() -> str:
    """Read DownloadClientConfig.

    GET /api/v1/config/downloadclient
    """
    return call("GET", "/api/v1/config/downloadclient", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_config_host() -> str:
    """Read HostConfig.

    GET /api/v1/config/host
    """
    return call("GET", "/api/v1/config/host", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_config_ui() -> str:
    """Read UiConfig.

    GET /api/v1/config/ui
    """
    return call("GET", "/api/v1/config/ui", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_customfilter() -> str:
    """Read CustomFilter.

    GET /api/v1/customfilter
    """
    return call("GET", "/api/v1/customfilter", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_downloadclient() -> str:
    """Read DownloadClient.

    GET /api/v1/downloadclient
    """
    return call("GET", "/api/v1/downloadclient", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_downloadclient_schema() -> str:
    """Read DownloadClient.

    GET /api/v1/downloadclient/schema
    """
    return call("GET", "/api/v1/downloadclient/schema", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_filesystem(path: str | None = None, include_files: bool | None = None, allow_folders_without_trailing_slashes: bool | None = None) -> str:
    """Read FileSystem.

    GET /api/v1/filesystem

    Args:
        path: Query parameter.
        include_files: Query parameter.
        allow_folders_without_trailing_slashes: Query parameter.
    """
    return call("GET", "/api/v1/filesystem", query={"path": path, "includeFiles": include_files, "allowFoldersWithoutTrailingSlashes": allow_folders_without_trailing_slashes}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_filesystem_type(path: str | None = None) -> str:
    """Read FileSystem.

    GET /api/v1/filesystem/type

    Args:
        path: Query parameter.
    """
    return call("GET", "/api/v1/filesystem/type", query={"path": path}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_health() -> str:
    """Read Health.

    GET /api/v1/health
    """
    return call("GET", "/api/v1/health", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_history(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None, event_type: list | None = None, successful: bool | None = None, download_id: str | None = None, indexer_ids: list | None = None) -> str:
    """Read History.

    GET /api/v1/history

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
        event_type: Query parameter.
        successful: Query parameter.
        download_id: Query parameter.
        indexer_ids: Query parameter.
    """
    return call("GET", "/api/v1/history", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction, "eventType": event_type, "successful": successful, "downloadId": download_id, "indexerIds": indexer_ids}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_history_indexer(indexer_id: int | None = None, event_type: dict | None = None, limit: int | None = None) -> str:
    """Read History.

    GET /api/v1/history/indexer

    Args:
        indexer_id: Query parameter.
        event_type: Query parameter.
        limit: Query parameter.
    """
    return call("GET", "/api/v1/history/indexer", query={"indexerId": indexer_id, "eventType": event_type, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_history_since(date: str | None = None, event_type: dict | None = None) -> str:
    """Read History.

    GET /api/v1/history/since

    Args:
        date: Query parameter.
        event_type: Query parameter.
    """
    return call("GET", "/api/v1/history/since", query={"date": date, "eventType": event_type}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_indexer() -> str:
    """Read Indexer.

    GET /api/v1/indexer
    """
    return call("GET", "/api/v1/indexer", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_indexer_categories() -> str:
    """Read IndexerDefaultCategories.

    GET /api/v1/indexer/categories
    """
    return call("GET", "/api/v1/indexer/categories", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_indexer_schema() -> str:
    """Read Indexer.

    GET /api/v1/indexer/schema
    """
    return call("GET", "/api/v1/indexer/schema", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_indexerproxy() -> str:
    """Read IndexerProxy.

    GET /api/v1/indexerproxy
    """
    return call("GET", "/api/v1/indexerproxy", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_indexerproxy_schema() -> str:
    """Read IndexerProxy.

    GET /api/v1/indexerproxy/schema
    """
    return call("GET", "/api/v1/indexerproxy/schema", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_indexerstats(start_date: str | None = None, end_date: str | None = None, indexers: str | None = None, protocols: str | None = None, tags: str | None = None) -> str:
    """Read IndexerStats.

    GET /api/v1/indexerstats

    Args:
        start_date: Query parameter.
        end_date: Query parameter.
        indexers: Query parameter.
        protocols: Query parameter.
        tags: Query parameter.
    """
    return call("GET", "/api/v1/indexerstats", query={"startDate": start_date, "endDate": end_date, "indexers": indexers, "protocols": protocols, "tags": tags}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_indexerstatus() -> str:
    """Read IndexerStatus.

    GET /api/v1/indexerstatus
    """
    return call("GET", "/api/v1/indexerstatus", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_localization() -> str:
    """Read Localization.

    GET /api/v1/localization
    """
    return call("GET", "/api/v1/localization", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_localization_options() -> str:
    """Read Localization.

    GET /api/v1/localization/options
    """
    return call("GET", "/api/v1/localization/options", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_log(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None, level: str | None = None) -> str:
    """Read Log.

    GET /api/v1/log

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
        level: Query parameter.
    """
    return call("GET", "/api/v1/log", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction, "level": level}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_log_file() -> str:
    """Read LogFile.

    GET /api/v1/log/file
    """
    return call("GET", "/api/v1/log/file", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_log_file_update() -> str:
    """Read UpdateLogFile.

    GET /api/v1/log/file/update
    """
    return call("GET", "/api/v1/log/file/update", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_login() -> str:
    """Read StaticResource.

    GET /login
    """
    return call("GET", "/login", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_logout() -> str:
    """Read Authentication.

    GET /logout
    """
    return call("GET", "/logout", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_notification() -> str:
    """Read Notification.

    GET /api/v1/notification
    """
    return call("GET", "/api/v1/notification", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_notification_schema() -> str:
    """Read Notification.

    GET /api/v1/notification/schema
    """
    return call("GET", "/api/v1/notification/schema", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_ping() -> str:
    """Read Ping.

    GET /ping
    """
    return call("GET", "/ping", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_root(path: str) -> str:
    """Read StaticResource.

    GET /

    Args:
        path: Path parameter.
    """
    return call("GET", "/", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_search(query: str | None = None, type_: str | None = None, indexer_ids: list | None = None, categories: list | None = None, limit: int | None = None, offset: int | None = None) -> str:
    """Read Search.

    GET /api/v1/search

    Args:
        query: Query parameter.
        type_: Query parameter.
        indexer_ids: Query parameter.
        categories: Query parameter.
        limit: Query parameter.
        offset: Query parameter.
    """
    return call("GET", "/api/v1/search", query={"query": query, "type": type_, "indexerIds": indexer_ids, "categories": categories, "limit": limit, "offset": offset}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_system_backup() -> str:
    """Read Backup.

    GET /api/v1/system/backup
    """
    return call("GET", "/api/v1/system/backup", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_system_routes() -> str:
    """Read System.

    GET /api/v1/system/routes
    """
    return call("GET", "/api/v1/system/routes", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_system_routes_duplicate() -> str:
    """Read System.

    GET /api/v1/system/routes/duplicate
    """
    return call("GET", "/api/v1/system/routes/duplicate", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_system_status() -> str:
    """Read System.

    GET /api/v1/system/status
    """
    return call("GET", "/api/v1/system/status", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_system_task() -> str:
    """Read Task.

    GET /api/v1/system/task
    """
    return call("GET", "/api/v1/system/task", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_tag() -> str:
    """Read Tag.

    GET /api/v1/tag
    """
    return call("GET", "/api/v1/tag", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_tag_detail() -> str:
    """Read TagDetails.

    GET /api/v1/tag/detail
    """
    return call("GET", "/api/v1/tag/detail", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_update() -> str:
    """Read Update.

    GET /api/v1/update
    """
    return call("GET", "/api/v1/update", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def update_applications_bulk(body: dict) -> str:
    """Update Application.

    PUT /api/v1/applications/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v1/applications/bulk", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_applications_by_id(id_: str, body: dict, force_save: bool | None = None) -> str:
    """Update Application.

    PUT /api/v1/applications/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v1/applications/{id_}", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_appprofile_by_id(id_: str, body: dict) -> str:
    """Update AppProfile.

    PUT /api/v1/appprofile/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/appprofile/{id_}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_config_development_by_id(id_: str, body: dict) -> str:
    """Update DevelopmentConfig.

    PUT /api/v1/config/development/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/config/development/{id_}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_config_downloadclient_by_id(id_: str, body: dict) -> str:
    """Update DownloadClientConfig.

    PUT /api/v1/config/downloadclient/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/config/downloadclient/{id_}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_config_host_by_id(id_: str, body: dict) -> str:
    """Update HostConfig.

    PUT /api/v1/config/host/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/config/host/{id_}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_config_ui_by_id(id_: str, body: dict) -> str:
    """Update UiConfig.

    PUT /api/v1/config/ui/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/config/ui/{id_}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_customfilter_by_id(id_: str, body: dict) -> str:
    """Update CustomFilter.

    PUT /api/v1/customfilter/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/customfilter/{id_}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_downloadclient_bulk(body: dict) -> str:
    """Update DownloadClient.

    PUT /api/v1/downloadclient/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v1/downloadclient/bulk", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_downloadclient_by_id(id_: str, body: dict, force_save: bool | None = None) -> str:
    """Update DownloadClient.

    PUT /api/v1/downloadclient/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v1/downloadclient/{id_}", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_indexer_bulk(body: dict) -> str:
    """Update Indexer.

    PUT /api/v1/indexer/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v1/indexer/bulk", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_indexer_by_id(id_: str, body: dict, force_save: bool | None = None) -> str:
    """Update Indexer.

    PUT /api/v1/indexer/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v1/indexer/{id_}", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_indexerproxy_by_id(id_: str, body: dict, force_save: bool | None = None) -> str:
    """Update IndexerProxy.

    PUT /api/v1/indexerproxy/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v1/indexerproxy/{id_}", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_notification_by_id(id_: str, body: dict, force_save: bool | None = None) -> str:
    """Update Notification.

    PUT /api/v1/notification/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v1/notification/{id_}", query={"forceSave": force_save}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_tag_by_id(id_: str, body: dict) -> str:
    """Update Tag.

    PUT /api/v1/tag/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/tag/{id_}", query=None, body=body, form=None)
