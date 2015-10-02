# coding: utf-8
import pandas
import pandas as pd

budget = pd.read_csv("mn-budget-detail-2014.csv")
budget = budget.sort('amount', ascending=False)[:10]
pd.options.display.mpl_style = 'default'
budget_plot = budget.plot(kind='bar', x=budget['detail'], title='MN Capital Budget - 2014',legend=False)
fig = budget_plot.get_figure()
fig.savefig("2014-mn-capital-budget-pandas.png")



import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
bar_plot = sns.barplot(x=budget['detail'],y=budget['amount'],palette='muted',order=budget['detail'].tolist())
bar_plot = sns.barplot(x=budget['detail'],y=budget['amount'],palette='muted',order=budget['detail'].tolist())
plt.xticks(rotation=90)
plt.show()
fig2 = bar_plot.get_figure()
fig2.savefig("2014-mn-capital-budget-seaborn.png")



from ggplot import *

p = ggplot(budget, aes(x='detail', y='amount'))+ \
geom_bar(stat='bar',labels=budget['detail'].tolist()) +\
ggtitle('MN Capital Budget - 2014') + \
xlab('Spending Detail')+\
ylab('Amount')+scale_y_continuous(labels='millions')+\
theme(axis_text_x=element_text(angle=90))
print p
ggsave(p, "mn-budget-capital-ggplot.png")



from bokeh.charts import Bar, output_file, show

bar = Bar(budget,'detail',values='amount',title='Title')
output_file('mn-budget-capital-bokeh-bar.html')
show(bar)



import pygal
from pygal.style import LightStyle
bar_chart = pygal.Bar(style=LightStyle, width=800, height=600,
                      legend_at_bottom=True, human_readable=True,
                      title='MN Capital Budget - 2014')
for index, row in budget.iterrows():
        bar_chart.add(row["detail"], row["amount"])
    
bar_chart.render_to_file('mn-budget-capital-pygal.svg')
bar_chart.render_to_file('mn-budget-capital-pygal.png')



import plotly.plotly as py
from plotly.graph_objs import *
data = Data([Bar(x=budget['detail'],y=budget['amount'])])
layout = Layout(title='2014 MN Capital Budget',font=Font(family='Raleway, sans-serif'),showlegend=False,xaxis=XAxis(tickangle=-45),bargap=0.05)
fig = Figure(data=data, layout=layout)

#########################
un = raw_input('INPUT USERNAME> ')
api_key = raw_input('INPUT API_KEY> ')
py.sign_in(un,api_key)
plot_url = py.plot(data,filename='MN Capital Budget - 2014')
py.image.save_as(fig, 'mn-14-budget-plotly.png')