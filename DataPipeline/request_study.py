import requests
import json
import random
import time
from bs4 import BeautifulSoup


def request_salud_digna(save=False):
    """ Pings  https://salud-digna.org/ and retrieves all the studies on Toluca Central
        It gives a json file of the form
        [
            {
                "Id": 68479,
                "Descripcion": "17 ALFA HIDROXI PROGESTERONA",
                "Preparacion": "AYUNO M�NIMO DE 4 HRS\r\n  \r\n\r\n\r\n",
                "Estudio": "LABORATORIO",
                "Fecha": null,
                "Horario": null,
                "Precio": "254.3103","""

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
        time.sleep(random.uniform(3, 5))
        estudios = ["analisis-clinicos",
                    "mastografia",
                    "ultrasonido",
                    "rayos-x",
                    "tomografia",
                    "electrocardiograma",
                    "papanicolau",
                    "densitometria"]
        urlStudies = ["https://api.emarketingsd.org/citas/citas/SubEstudiosPorSucursalPP?estudio%5BId%5D=2&sucursal%5BId%5D=101&filtro=1&busqueda=",
        "https://api.emarketingsd.org/Citas/Citas2/SubEstudiosPorSucursal?idEstudio=3&idSucursal=101&filtro=1&busqueda=&origen=0",
        "https://api.emarketingsd.org/citas/citas/SubEstudiosPorSucursalPP?estudio%5BId%5D=6&sucursal%5BId%5D=101&filtro=1&busqueda=",
        "https://api.emarketingsd.org/Citas/Citas2/SubEstudiosPorSucursal?idEstudio=5&idSucursal=101&filtro=1&busqueda=&origen=0",
        "https://api.emarketingsd.org/Citas/Citas2/SubEstudiosPorSucursal?idEstudio=11&idSucursal=101&filtro=1&busqueda=&origen=0",
        "https://api.emarketingsd.org/Citas/Citas2/SubEstudiosPorSucursal?idEstudio=9&idSucursal=101&filtro=1&busqueda=&origen=0",
        "https://api.emarketingsd.org/Citas/Citas2/SubEstudiosPorSucursal?idEstudio=4&idSucursal=101&filtro=1&busqueda=&origen=0",
        "https://api.emarketingsd.org/Citas/Citas2/SubEstudiosPorSucursal?idEstudio=4&idSucursal=101&filtro=1&busqueda=&origen=0"]
        
        save_data = {}
        for i in range(len(estudios)):
            time.sleep(random.uniform(1,2))
            rStudies = s.get(url=urlStudies[i], headers=headers)
            assert rStudies.status_code == 200
            data = rStudies.json()
            if estudios[i] == 'analisis-clinicos' or estudios[i] == 'ultrasonido':
                save_data[estudios[i]] = data
            else:
                save_data[estudios[i]] = data['data']
            # print(type(save_data))
        #save_data = json.dumps(save_data, ensure_ascii=False, indent=2)
        if save == True:
            with open("response_salud_digna.json", 'w',encoding='utf-8') as studies:
                json.dump(save_data, studies, ensure_ascii=False)
        return save_data


def request_laboratorio_medico_polanco(save=False):
    """ Pings  https://lmpolanco.com/estudios and retrieves all the studies
        It gives a json file of the form
        "analisis-clinicos": [
                                {
                                    "id": 1,
                                    "department_id": 1,
                                    "image": "SANGRE_1.jpg",
                                    "type": "E",
                                    "title": "11 DESOXICORTISOL",
                                    "scheduled": "0",
                                    "tags": null,
                                    "indications": null,
                                    "description": null,
                                    "price_list": "7508"
                                ...
                                ...
                                ...,
        "audiometria": [
                                {
                                    "id": 593,
                                    "department_id": 30,
                                    "image": "AUDIOMETRIA1",
                                    "type": "E",
                                    "title": "AUDIOMETRIA (CON INTERPRETACION)",
                                    "scheduled": "0",
                                    "tags": null,
                                    "indications": "\n- Presentar receta médica. \n- Edad mínima para realizar el estudio es de 8 a años.\n",
                                    "description": null,
                                    "price_list": "1026","""
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
        urlPrep = "https://lmpolanco.com/estudios"
        r = s.get(url=urlPrep, headers=headers)
        assert r.status_code == 200

        urlDepartaments = "https://lmpolanco.com/general-home"
        rDepartaments = s.get(url=urlDepartaments, headers=headers)
        assert rDepartaments.status_code == 200

        jsonDepartments = rDepartaments.json()
        jsonDepartments = jsonDepartments['departments']

        save_data = {}

        for department in jsonDepartments:

            time.sleep(random.uniform(3, 5))
            requestDepartment = s.get(
                url="https://lmpolanco.com/departments-studies/"+department['url'], headers=headers)
            assert requestDepartment.status_code == 200
            dataDepartment = requestDepartment.json()['departments']
            save_data[department['url']] = dataDepartment

        save_data = json.dumps(save_data, ensure_ascii=False, indent=2)

        if save == True:
            with open("response_laboratorio_medico_polanco.json", 'w', encoding="utf-8") as studies:
                studies.write(save_data)

        return save_data


def request_monar(save=False):
    """ Pings  http://www.laboratoriomonar.com/{estudio}/ and retrieves all the studies
        It gives a json file of the form
       {
            "analisis-clinicos": {
                "Ácido Úrico": "\nEntrega: Mismo día\t\t\t\t\t\t\t\t\t\nPreparación: Ayuno\t\t\t\t\t\t\t\t\t\nCosto: $50 \r\n\t\t\t\t\t\t\t\t",
                "Ácidos Grasos Libres en suero": "\nEntrega: Mismo día\t\t\t\t\t\t\t\t\t\nPreparación: Ayuno\t\t\t\t\t\t\t\t\t\nCosto: $470.00 \r\n\t\t\t\t\t\t\t\t",

                ...
                ...
                ...,
            "audiometria": {
                "Audiometría Tonal": "\nEntrega: Mismo día\t\t\t\t\t\t\t\t\t\nPreparación: Ninguna\t\t\t\t\t\t\t\t\t\nCosto: $300.00 \r\n\t\t\t\t\t\t\t\t"
        """
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
        estudios = ["analisis-clinicos",
                    "audiometria",
                    "densitometria",
                    "electrocardiograma",
                    "electroencefalograma/",
                    "espirometria",
                    "mastografia",
                    "rayos-x",
                    "tomografia",
                    "ultrasonido"]
        save_data = {}
        for estudio in estudios:
            time.sleep(random.uniform(3, 5))
            r = s.get(
                url=f"http://www.laboratoriomonar.com/{estudio}/", headers=headers)
            assert r.status_code == 200
            soup = BeautifulSoup(r.text, 'lxml')

            studies = soup.find_all('dd')
            save_data_study = {}
            for i in range(len(studies)):
                if i % 2 == 0:
                    save_data_study[studies[i].text] = ''
                else:

                    save_data_study[studies[i-1].text] = studies[i].text
            save_data[estudio] = save_data_study

        save_data = json.dumps(save_data, ensure_ascii=False, indent=2)

        if save == True:
            with open("response_monar.json", 'w', encoding="utf-8") as studies:
                studies.write(save_data)


        return save_data

def request_olab(save=False):
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
        save_data = {}
        estudios = ["estudios-de-laboratorio",
                    "rayos-x",
                    "estudios-especiales",
                    "resonancia-magnetica",
                    "tomografia",
                    "ultrasonido"]
        api_estudios = ["https://www.olab.com.mx/bp/olab_labs.json?_=1618894740985",
                        "https://www.olab.com.mx/bp/olab_gab.json?_=1618894758753",
                        "https://www.olab.com.mx/bp/olab_esp.json?_=1618894781416",
                        "https://www.olab.com.mx/bp/olab_resm.json?_=1618894801150",
                        "https://www.olab.com.mx/bp/olab_resm.json?_=1618894801150",
                        "https://www.olab.com.mx/bp/olab_ult.json?_=1618894829760"]
        url = "https://www.olab.com.mx/estudios-de-laboratorio/"

        for i in range(len(estudios)):
            time.sleep(random.uniform(3, 5))
            r = s.get(url=f"https://www.olab.com.mx/{estudios[i]}/",headers=headers)
            assert r.status_code == 200
            rData = s.get(url=api_estudios[i],headers=headers)
                                
            assert rData.status_code == 200

            save_data[estudios[i]] = rData.json()['data']
        save_data = json.dumps(save_data, ensure_ascii=False, indent=2)

        if save == True:
            with open("response_olab.json", 'w', encoding="utf-8") as studies:
                studies.write(save_data)


        return save_data

if __name__ == "__main__":
    request_salud_digna(save = True)
