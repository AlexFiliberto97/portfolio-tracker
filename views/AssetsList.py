
import flet as ft

#create asset list page table header
def build_table_header():
    return ft.Container(
        bgcolor="#1E1E1E",
        padding=ft.Padding.symmetric(horizontal=20, vertical=12),
        content=ft.Row([
            ft.Text("", width=40), #icon
            ft.Text("NAME", expand=2, color="#9E9E9E", weight="bold", text_align="left", size=13),
            ft.Text("SYMBOL", expand=1, color="#9E9E9E", weight="bold", text_align="center", size=13),
            ft.Text("ISIN", expand=1, color="#9E9E9E", weight="bold", text_align="center", size=13),
            ft.Text("PRICE", expand=1, color="#9E9E9E", weight="bold", text_align="center", size=13),
            ft.Text("Δ", expand=1, color="#9E9E9E", weight="bold", text_align="center", size=13),
            ft.Text("Δ (amount)", expand=1, color="#9E9E9E", weight="bold", text_align="center", size=13),
            ft.Text("MARKET STATUS", expand=1, color="#9E9E9E", weight="bold", text_align="center", size=13)
        ], spacing=0)
    )

#create table rows
def build_table_row(asset):

    #price change labels
    price_label = ft.Text(asset.price, expand=1, color="#B3B3B3", text_align="center")
    price_delta_label = ft.Text(asset.price_delta, expand=1, color="#B3B3B3", text_align="center")
    price_delta_percentage_label = ft.Text(asset.price_delta_percentage, expand=1, color="#B3B3B3", text_align="center")
    market_status_label = ft.Text(asset.market_status, expand=1, color="#B3B3B3", text_align="center")

    #building the row
    asset_row_container = ft.Container(
        padding=ft.Padding.symmetric(horizontal=20, vertical=15),
        border=ft.Border.only(bottom=ft.BorderSide(1, "#3a3a3a")),
        content=ft.Row([

            #asset icon
            ft.Container(
                content=ft.Image(
                    src=asset.icon_path,
                    width=24,
                    height=24,
                    fit=ft.Image.fit,
                ),
                width=40,
            ),

            #asset name (link to asset detail page)
            ft.Container(
                content=ft.Text(asset.name, weight="bold", color="#B3B3B3"),
                expand=2,
                on_click=lambda e: print(e), #todo: implement
            ),

            #asset immutable labels
            ft.Text(asset.ticker, expand=1, color="#B3B3B3", text_align="center"),
            ft.Text(asset.isin, expand=1, color="#B3B3B3", text_align="center"),

            #asset mutable labels
            price_label,
            price_delta_label,
            price_delta_percentage_label,
            market_status_label,
        ], spacing=0)
    )

    return asset_row_container, price_label, price_delta_label, price_delta_percentage_label, market_status_label


def build_asset_list_view(assets):

    #building table rows and assets price labels dict
    table_rows = []
    asset_price_labels = {}
    for asset in assets:
        asset_row_container, price_label, price_delta_label, price_delta_percentage_label, market_status = build_table_row(asset)
        table_rows.append(asset_row_container)
        asset_price_labels[asset.ticker] = {
            "price_label": price_label,
            "price_delta_label": price_delta_label,
            "price_delta_percentage_label": price_delta_percentage_label,
            "market_status_label": market_status
        }

    #creating asset list view
    asset_list_view = ft.Column([
        build_table_header(),
        ft.Column(
            controls=table_rows,
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE,
            expand=True
        )
    ], expand=True, spacing=0)
    return asset_list_view, asset_price_labels

