from dtlpy.utilities.reports import Report, Table, Line, Scatter, Bar, Hbar, Doughnut, Pie, FigOptions, ConfusionMatrix
import dtlpy as dl

table = Table(title="table example3",
              labels=["col1", "col2", "col3"],
              data=[[1, 2, 3]],
              options={})

doughnut = Doughnut(title="doughnut example (id = 22)",
                    title_href=None,
                    plot_id='22',
                    labels=["red", "green", "blue"],
                    data=[20, 30, 150],
                    options=FigOptions(colors=["red", "green", "blue"]))

line = Line(title="lines example",
            labels=[1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1999, 2050],
            data=[
                {"label": "Africa",
                 "value": [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478]},
                {"label": "Asia",
                 "value": [282, 350, 411, 502, 635, 809, 947, 1402, 3700, 5267]},
                {"label": "Europe",
                 "value": [86, 114, 106, 106, 107, 111, 150, 250, 800, 2550]}
            ],
            options={}
            )
scatter = Scatter(title="scatter example",
                  data=[
                      {"label": "Male",
                       "value": [{"x": -10, "y": 0}, {"x": 0, "y": 10}, {"x": 10, "y": 5}, {"x": 0.5, "y": 5.5}]
                       },
                      {"label": "Female",
                       "value": [{"x": -5, "y": 0}, {"x": 1, "y": 1}, {"x": 7, "y": 9}, {"x": 15.9, "y": -6.5}]
                       }],
                  options={}
                  )

line = Line(title="lines example",
            labels=[1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1999, 2050, 4000, 4001, 4002, 1500, 1600, 1700,
                    1750, 1800, 1850, 1900, 1950, 1999, 2050, 4000, 4001, 4002, 1500, 1600, 1700, 1750, 1800, 1850,
                    1900, 1950, 1999, 2050, 4000, 4001, 4002],
            data=[{"label": "Africa",
                   "value": [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478]},
                  {"label": "Asia",
                   "value": [282, 350, 411, 502, 635, 809, 947, 1402, 3700, 5267]},
                  {"label": "Europe",
                   "value": [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478]}
                  ]
            )

pie = Pie(title="pie example",
          labels=["red", "green", "blue"],
          data=[20, 30, 150])

bar = Bar(title="bars example (id = 33)",
          plot_id="33",
          labels=["@@@@@@@", "Asia", "Europe", "Latin America", "North America", "Africa", "Asia", "Europe",
                  "Latin America", "North America", "Africa", "Asia", "Europe", "Latin America", "North America",
                  "Africa", "Asia", "Europe", "Africa", "Asia", "Europe", "Africa", "Asia", "Europe", "Africa", "Asia",
                  "Europe", "Africa", "Asia", "Europe", "Africa", "Asia", "Europe", "Latin America", "North America",
                  "Africa", "Asia", "Europe", "Latin America", "North America", "Africa", "Asia", "Europe",
                  "Latin America", "North America", "Africa", "Asia", "Europe", "Africa", "Asia", "Europe", "Africa",
                  "Asia", "Europe", "Africa", "Asia", "Europe", "Africa", "Asia", "Europe"],
          data=[{"label": "Population (millions)",
                 "value": [2478, 5267, 734, 784, 433, 2478, 5267, 734, 784, 433, 2478, 5267, 734, 784, 433, 2478, 5267,
                           734, 784, 433, 2478, 5267, 734, 784, 433, 2478, 5267, 734, 784, 433, 2478, 5267, 734, 784,
                           433, 2478, 5267, 734, 784, 433, 2478, 5267, 734, 784, 433, 2478, 5267, 734, 784, 433, 2478,
                           5267, 734, 784, 433, 2478, 5267, 734, 784, 433]}],
          )
bar = Bar(title="bars example with horizontal",
          labels=["Africa", "Asia", "Europe", "Latin America", "North America"],
          data=[{"label": "Population (millions)",
                 "value": [2478, 5267, 734, 784, 433]}
                ],
          options=FigOptions(direction="horizontal")
          )
hbar = Hbar(title="hbars example",
            labels=["Africa", "Asia", "Europe", "Latin America", "North America"],
            data=[
                {"label": "Population (millions)",
                 "value": [2478, 5267, 734, 784, 433]}
            ])
table = Table(
    title="table example",
    labels=["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13",
            "col14", "col15"],
    data=[[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
          [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
          [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
          [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
          [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]],
    options=FigOptions(rows_per_page=1000)
)

# using hrefs for platform and external links
table = Table(title="table example",
              title_href="https://local.dataloop.ai:8443/projects/",
              plot_id="11",
              labels=["col1", "col2", "col3"],
              data=[[{"text": "Link to Graph 22",
                      "href": "#22"},
                     2,
                     {"text": "Go to Google",
                      "href": "https://www.google.com/"}],
                    [{"text": "Not existing graph id",
                      "href": "#55"},
                     {"text": "Link to Graph 33",
                      "href": "#33"},
                     {"text": "Go to Google2",
                      "href": "htaaaatps://www.google.com/"}],
                    [1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]
                    ],
              options=FigOptions(rows_per_page=1000)
              )

# confusion matrix with href links and color pallet
from sklearn.metrics import confusion_matrix
import seaborn as sns

filters = dl.Filters()
href = filters.platform_url(resource=dl.datasets.get(dataset_id='607ed8107370454e4dd3b4c7'))
y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
colors = sns.color_palette("rocket", as_cmap=True)
data = confusion_matrix(y_true, y_pred,
                        labels=["ant", "bird", "cat"],
                        normalize='true')
color_map = colors(data)
href_map = [[href for _ in range(data.shape[0])] for _ in range(data.shape[0])]
confusion = ConfusionMatrix(title="confusion example, threshold > 0.5",
                            labels=["ant", "bird", "cat"],
                            data=data,
                            color_map=color_map,
                            href_map=href_map,
                            options=FigOptions(rows_per_page=100,
                                               x_title="true",
                                               y_title="pred"))

#####################
# Define the layout #
#####################
report = Report(ncols=2, nrows=2)

# Add the figures
report.add(fig=scatter, icol=0, irow=0)
report.add(fig=table, icol=0, irow=1)
report.add(fig=doughnut, icol=1, irow=0)
report.add(fig=bar, icol=1, irow=1)

# Upload the report to a dataset
report.upload(dataset=dl.datasets.get(dataset_id="datasetId"),
              remote_path="/",
              remote_name="reports examples.json")
