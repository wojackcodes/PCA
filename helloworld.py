import vl_convert as vlc, json

spec = json.load(open("chart.vl.json"))
open("chart.svg", "w").write(vlc.vega_to_svg(spec))
open("chart.png", "wb").write(vlc.vega_to_png(spec, scale=2))
