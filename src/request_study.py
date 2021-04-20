import requests
import json


def request_salud_digna(save=False):
    with requests.Session() as s:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'es-MX,es;q=0.9,en-US;q=0.8,en;q=0.7,es-419;q=0.6',
        }
        urlPrep = "https://salud-digna.org/precios-preparaciones/"
        r = s.get(url=urlPrep, headers=headers)
        assert r.status_code == 200

        urlStudies = "https://api.emarketingsd.org/citas/citas/SubEstudiosPorSucursalPP?estudio%5BId%5D=2&sucursal%5BId%5D=101&filtro=1&busqueda="
        rStudies = s.get(url=urlStudies, headers=headers)
        assert rStudies.status_code == 200

        save_data = json.dumps(rStudies.json(), ensure_ascii=False, indent=2)
        # print(type(save_data))

        if save == True:
            with open("response_salud_digna.json", 'w') as studies:
                studies.write(save_data)
        return save_data


if __name__ == "__main__":
    request_salud_digna(save=True)
