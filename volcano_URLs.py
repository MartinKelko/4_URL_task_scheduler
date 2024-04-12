import webbrowser
import schedule
import time

# List of URLs volcano observatories to open
urls = [
    'https://laculturevolcan.blogspot.com/',
    'https://www.volcanocafe.org/',
    'https://volcano.si.edu/reports_weekly.cfm',
    'https://www.usgs.gov/',
    'https://www.usgs.gov/observatories/hvo',
    'https://www.hawaiitracker.com/',
    'https://avo.alaska.edu/',
    'https://www.gob.mx/cenapred',
    'https://insivumeh.gob.gt/?p=89647',
    'https://insivumeh.gob.gt/?p=92961',
    'https://insivumeh.gob.gt/?p=97000',
    'https://elobservatorio.marn.gob.sv/',
    'https://www.ineter.gob.ni/#vigilanciasismo',
    'http://www.ovsicori.una.ac.cr/index.php/vulcanologia/informes-y-boletines/boletin-semanal-vigilancia-volcanica',
    'https://www.sgc.gov.co/',
    'https://www.igepn.edu.ec/servicios/busqueda-informes',
    'https://www.igp.gob.pe/servicios/centro-vulcanologico-nacional/',
    'https://www.gob.pe/igp',
    'https://www.sernageomin.cl/',
    'https://us19.campaign-archive.com/home/?u=74e140ef75e59848ab401b24d&id=c811776a51',
    'https://www.povi.cl/',
    'https://mvoms.org/',
    'http://nemo.gov.vc/nemo/',
    'https://ovg-rdc.cd/',
    'http://geo-gsnl.org/supersites/permanent-supersites/virunga-supersite/',
    'https://www.virunga-volcanoes.org/',
    'https://www.ipgp.fr/communiques-et-bulletins-de-lobservatoire/?categorie=&domaine=&date=&observatoire-associe=391&motcle=',
    'https://en.vedur.is/',
    'https://jardvis.hi.is/is',
    'https://www.almannavarnir.is/english/',
    'https://www.ruv.is/',
    'https://www.icelandreview.com/',
    'https://www.ct.ingv.it/index.php/monitoraggio-e-sorveglianza/prodotti-del-monitoraggio/comunicati-attivita-vulcanica',
    'https://www.ct.ingv.it/index.php/monitoraggio-e-sorveglianza/segnali-in-tempo-reale/tremore-vulcanico',
    'https://www.ct.ingv.it/index.php/monitoraggio-e-sorveglianza/segnali-in-tempo-reale/video-sorveglianza-vulcanica-etna',
    'https://www.ct.ingv.it/index.php/monitoraggio-e-sorveglianza/segnali-in-tempo-reale/video-sorveglianza-vulcanica-isole-eolie',
    'http://lgs.geo.unifi.it/stromboli/str.php',
    'https://www.ilvulcanoapiedi.it/webcam-stromboli/',
    'https://www.ign.es/web/ign/portal/noticias',
    'http://www.kscnet.ru/ivs/kvert/index?lang=en',
    'http://volkstat.ru/',
    'http://www.imgg.ru/ru',
    'https://www.data.jma.go.jp/svd/vois/data/tokyo/STOCK/volinfo/volinfo.php',
    'https://www.jma.go.jp/bosai/map.html#5/37.996/135/&contents=volcano&lang=en',
    'http://www1.kaiho.mlit.go.jp/kaiikiDB/kaiyo18-2.htm#photograph',
    'https://magma.esdm.go.id/v1/gunung-api/informasi-letusan#',
    'https://magma.esdm.go.id/v1/gunung-api/laporan?page=1',
    'https://vsi.esdm.go.id/',
    'https://www.phivolcs.dost.gov.ph/volcano-hazard/volcano-bulletin2/mayon-volcano',
    'https://www.phivolcs.dost.gov.ph/volcano-hazard/volcano-bulletin2/taal-volcano',
    'https://www.phivolcs.dost.gov.ph/volcano-hazard/volcano-bulletin2/pinatubo-volcano',
    'https://www.phivolcs.dost.gov.ph/volcano-hazard/volcano-bulletin2/kanlaon-volcano',
    'https://www.phivolcs.dost.gov.ph/volcano-hazard/volcano-bulletin2/bulusan-volcano',
    'https://www.geonet.org.nz/volcano/vab',
    'https://www.vmgd.gov.vu/vmgd/index.php/geohazards/volcano/alert-bulletin',
    'https://www.facebook.com/vmgd.gov.vu',
    'https://www.facebook.com/tongageologicalservice',
    'https://volcanodiscovery.com/?t',
    'https://www.mirovaweb.it/',
    'https://pics.volcanodiscovery.org/browseImages.php',
    'https://www.volcanodiscovery.com/volcanoes.html',
    'https://translate.google.sk/?hl=en&tab=wT',
]

for url in urls:
        webbrowser.open(url)
        time.sleep(0.5)
def schedule_open_urls():
    # Run the `open_urls` function daily at 04:25 AM
    schedule.every().day.at("04:25").do(open_urls)

    # Infinite loop to continuously check for scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(0.5)

if __name__ == "__main__":
    schedule_open_urls()