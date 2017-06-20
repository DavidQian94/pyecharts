import json
from pprint import pprint
from echarts.option import Option

class Base():

    def __init__(self, title,
                 subtitle,
                 background_color="#fff",
                 width=800,
                 height=400,
                 title_pos="auto",
                 title_color="#000",
                 subtitle_color="#aaa",
                 title_text_size=18,
                 subtitle_text_size=12):
        self.Option = Option()
        self._option = {}
        self._width, self._height = width, height
        self._colorlst = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#749f83',
                          '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3']
        self._option.update(
            title={"text": title,
                   "subtext": subtitle,
                   "left": title_pos,
                   "textStyle": {"color": title_color, "fontSize": title_text_size},
                   "subtextStyle": {"color": subtitle_color, "fontSize": subtitle_text_size}
                  },
            tooltip={},
            series=[],
            legend={"data": []},
            backgroundColor=background_color
        )

    def add(self,
            label_show=None,
            label_pos=None,
            label_color=None,
            label_text_color=None,
            label_text_size=None,
            formatter=None,
            legend_show=None,
            legend_pos=None,
            legend_orient=None,
            line_width=None,
            line_opacity=None,
            line_type=None,
            split_line_show=None,
            axis_line_show=None,
            split_area_show=None,
            split_area_opacity=None,
            xy_font_size=None,
            nameGap=None,
            xaxis_name=None,
            xaxis_name_pos=None,
            interval=None,
            yaxis_name=None,
            yaxis_name_pos=None,
            exchange=None,
            x_axis=None,
            mark_line=None,
            mark_point=None,
            radius=None,
            center=None,
            rose_type=None,
            rand_data=None,
            layout=None,
            symbol_size=None,
            repulsion=None,
            smooth=None,
            shape=None,
            emphasis=None):
        pass

    def show_config(self):
        pprint(self._option)

    def render(self, path=r"..\render.html"):
        temple = r"..\temple\temple.html"
        try:
            if self._option.get("series")[0].get("type", None) in ("radar", "graph", "funnel") \
                    or self._option.get("series")[0].get('type', None) == "gauge":
                temple = r"..\temple\_temple.html"
        except:
            pass
        with open(temple, "r", encoding="utf-8") as f:
            my_option = json.dumps(self._option, indent=4, ensure_ascii=False)
            open(path, "w+", encoding="utf-8").write(
                f.read().replace("myOption", my_option)
                .replace("myWidth", str(self._width))
                .replace("myHeight", str(self._height))
            )
