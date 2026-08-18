import argparse
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from .zensical_cli import DEFAULT_CONFIG, build_zensical_site


def serve_zensical_site(
    project_dir,
    config_name=DEFAULT_CONFIG,
    zensical=None,
    strict=False,
    host="127.0.0.1",
    port=8001,
):
    site_dir = build_zensical_site(
        project_dir,
        config_name=config_name,
        zensical=zensical,
        strict=strict,
    )
    handler = partial(SimpleHTTPRequestHandler, directory=str(site_dir))
    server = ThreadingHTTPServer((host, port), handler)
    print(f"Servidor Zensical disponible en http://{host}:{port}/")
    print("Prem Ctrl+C per aturar-lo.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor aturat.")
    finally:
        server.server_close()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera un lloc Zensical amb les taules ODS i el serveix en local."
    )
    parser.add_argument(
        "--project-dir",
        default=os.getcwd(),
        help="Directori amb zensical.toml. Per defecte, el directori actual.",
    )
    parser.add_argument(
        "--config-file",
        default=DEFAULT_CONFIG,
        help=f"Nom del fitxer de configuració. Per defecte: {DEFAULT_CONFIG}.",
    )
    parser.add_argument("--zensical", help="Ruta alternativa al binari de Zensical.")
    parser.add_argument("--strict", action="store_true", help="Activa la compilació estricta.")
    parser.add_argument("--host", default="127.0.0.1", help="Adreça d'escolta.")
    parser.add_argument("--port", type=int, default=8001, help="Port HTTP. Per defecte: 8001.")
    return parser.parse_args()


def main():
    args = parse_args()
    serve_zensical_site(
        args.project_dir,
        config_name=args.config_file,
        zensical=args.zensical,
        strict=args.strict,
        host=args.host,
        port=args.port,
    )


if __name__ == "__main__":
    main()
