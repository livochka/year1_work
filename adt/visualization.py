# Created to visualize the information
# The part of adt package

import plotly.figure_factory as ff
import plotly as py
import plotly.graph_objs as go


class Visualize:
    """
    Created to visualization of information
    """

    def __init__(self):
        self.changes = {}

    def plot(self):
        """
        Plots the graph of information saved in self.changes dict
        x-axis - keys, y-axis - values
        """
        df = self.changes
        data = [go.Scatter(x=list(df.keys()), y=list(df.values()),
                           mode='lines+markers', line=dict(color='rgb(0,0,'
                                                                 '0)'))]
        py.offline.plot(data, filename='exchange.html')

    def histogram(self):
        """
        Plots the histogram of information saved in self.changes dict
        x-axis - keys, y-axis - values
        """
        x = list(self.changes.values())
        hist_data = [x]
        group_labels = ['Exchange rates distribution']
        colors = ['#A56CC1']
        fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                                 bin_size=1, show_rug=False)
        fig['layout'].update(title='Exchange rates distribution')

        py.offline.plot(fig, filename='Exchange rates distribution.html')
