import threading

from modules.Asset import Asset
from views import AssetsList
import flet_charts as fch
import flet as ft
import random
import time

#import requests
#import json
#import threading

CANDLE_DATA = [
    (0, 24.8, 28.6, 23.9, 27.2),
    (1, 27.2, 30.1, 25.8, 28.4),
    (2, 28.4, 31.2, 26.5, 29.1),
    (3, 29.1, 32.4, 27.9, 31.8),
    (4, 31.8, 34.0, 29.7, 30.2),
    (5, 30.2, 33.6, 28.3, 32.7),
    (6, 32.7, 35.5, 30.1, 34.6),
]

def sborrachart():
    return fch.CandlestickChart(
        min_x=0,
        max_x=30,
        min_y=0,
        max_y=50,
        #bgcolor=ft.Colors.AMBER_200,
        spots=[
            fch.CandlestickChartSpot(
                x=c[0],
                open=c[1],
                high=c[2],
                low=c[3],
                close=c[4],
            )

            for c in CANDLE_DATA
        ],
    )

def create_fast_chart():
    return fch.LineChart(
        data_series=[
            fch.LineChartData(
                points=[
                    fch.LineChartDataPoint(0, 140),
                    fch.LineChartDataPoint(1, 148),
                    fch.LineChartDataPoint(2, 142),
                    fch.LineChartDataPoint(3, 155),
                    fch.LineChartDataPoint(4, 151),
                    fch.LineChartDataPoint(5, 160),
                ],
                curved=True,             # Linea morbida (Spline)
                stroke_width=3,
                color=ft.Colors.CYAN_ACCENT,
                # L'area sotto la linea con gradiente
                below_line_bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.CYAN_ACCENT),
                below_line_gradient=ft.LinearGradient(
                    #begin=ft.Alignment,
                    #end=ft.alignment.bottom_center,
                    colors=[ft.Colors.with_opacity(0.2, ft.Colors.CYAN_ACCENT), ft.Colors.TRANSPARENT]
                ),
            )
        ],
        # Estetica scura e minimalista
        border=ft.Border.all(0, ft.Colors.TRANSPARENT),
        horizontal_grid_lines=fch.ChartGridLines(color="#262626", width=1),
        vertical_grid_lines=fch.ChartGridLines(color="#262626", width=1),
        left_axis=fch.ChartAxis(),
        bottom_axis=fch.ChartAxis(),
        expand=True,
    )

#def motore_prezzi(froci):
#    time.sleep(20)
#    print("start")
#    while True:
#        for f in froci:
#            widget = froci[f]

            # 2. Cambiamo il valore testuale
#            widget.value = f"{random.randint(10, 100)}"

            # 3. Opzionale: Cambiamo colore in base al movimento (effetto blink)
            #widget.color = ft.Colors.GREEN_ACCENT
            # 4. Fondamentale: diciamo a Flet di ridisegnare SOLO questo widget
#            widget.update()

#        time.sleep(10)

#####################################################################################################



def update_shit(assets, asset_price_labels):

    while True:
        for asset in assets:
            dio = asset_price_labels[asset.ticker]
            widget = dio["price_label"]
            if widget.page:
                print("update..")
                asset.update_asset_price()
                widget.value = asset.price
                widget.update()

        time.sleep(10)





def main(page: ft.Page):

    #page parameters
    page.title = "Modern Portfolio Tracker"
    page.window_width = 1200
    page.window_height = 720
    page.window_resizable = False
    page.window_maximizable = False
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#1a1a1a"



    #top bar
    top_bar = ft.Container(
        bgcolor="#0d0d0d",
        height=50,
        padding=ft.Padding.symmetric(horizontal=20),
        border=ft.Border.only(bottom=ft.BorderSide(1, "#3a3a3a")),
        #content=ft.Row([
        #    ft.Text("PORTFOLIO MANAGER", color="white", weight="bold", size=14)
        #])
    )

    #navigation rail
    rail_container = ft.Container(
        content=ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.NONE,
            group_alignment=0,
            bgcolor="#242424",
            min_width=70,
            destinations=[
                ft.NavigationRailDestination(icon=ft.Icons.QUERY_STATS, label="Assets"),
                ft.NavigationRailDestination(icon=ft.Icons.SETTINGS_OUTLINED, label="Settings"),
            ],
        ),
        border=ft.Border.only(right=ft.BorderSide(1, "#3a3a3a")),
    )

    assets = [
        Asset("Vanguard Ftse All-World Ucits E", "VWCE.MI", "IE00BK5BQT80", "vwce.png"),
        Asset("Bitcoin", "BTC", "-", "btc.png"),
        Asset("Tesla Inc.", "TSLA", "-", "pokemon.png")
    ]

    assets_list_view, asset_price_labels = AssetsList.build_asset_list_view(assets)
    main_view_container = ft.Container(content=assets_list_view, expand=True)

    #page final view
    page.add(
        top_bar,
        ft.Row(
            [
                rail_container,
                main_view_container

            ],
            expand=True,
            spacing=0
        )
    )

    t = threading.Thread(target=update_shit, args=(assets, asset_price_labels))
    t.start()


if __name__ == "__main__":
    ft.run(main=main, assets_dir="assets")
    #res = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCEUR")