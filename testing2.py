# -*- coding: utf-8 -*-

########################################################
#                       PACKAGES                       #
########################################################
import random
import plotly.plotly as py
import plotly.graph_objs as go
from sample import sample
import csv

########################################################
#                      FUNCTIONS                       #
########################################################

def pickColor():
    """
    Creates a string object refering to an hex color chosen randomly among a pre-set list
    :return: string
    """
    color = random.choice(['#003399', '#0033ff', '#006600', '#006699', '#009933','#00cc66', '#00cc33', '#00ff33', '#00ffcc',
                           '#330033', '#3300cc', '#333333', '#3333ff', '#336666', '#660099', '#660000', '#663333', '#666600',
                           '#666600', '#66cc33', '#990033', '#993300', '#990066', '#999933', '#999999', '#99cc00', '#cc0033',
                           '#cc3300', '#cc3333', '#cc3366', '#cc33ff', '#cc9900', '#ccff99', '#ff0033', '#ff3300', '#ff9900',
                           '#ffcc00', '#ffcc33', '#ffff33', '#ff0000', '00ff00', '0000ff'])
    return color


def createTile(listname):
    """
    Creates a title for the chart
    :param listname: list
    :return: string
    """
    pivot = random.choice([' confrontés aux ', ' en fonction des ', ' comparés aux ', ' au prisme des ', ' croisés avec les', ' à la lumière des ', ' mis en rapport avec les '])
    if len(listname) > 2:
        title = 'Les ' + str(listname[0]) + str(pivot) + str(listname[1]) + ' (et autres données)'
    else:
        title = 'Les ' + str(listname[0]) + str(pivot) + str(listname[1])
    return title


def createDataBar(xData, yData, name, orientation):
    """
    Creates a bar object for bar charts
    :param xData: list
    :param yData: list
    :param name: string
    :param orientation: string
    :return: bar object
    """
    color1 = pickColor()
    color2 = pickColor()
    # Chosing lining style
    line = random.choice([True, False])
    if line == True:
        marker = dict(color=color1, line=dict(color=color2, width=0.5))
    else:
        marker = dict(color=color1, opacity=1)
    # Creating the bar object to return
    barTrack = go.Bar(
        x=xData,
        y=yData,
        name=name,
        orientation=orientation,
        marker=marker
        )
    return barTrack


def createDataLine(xData, yData, name):
    """
    Creates a scatter object for line charts
    :param xData: list
    :param yData: list
    :param name: string
    :return: scatter object
    """
    mode = random.choice(['lines', 'lines+markers'])
    shape = random.choice(['hvh', 'spline', 'linear'])
    color = pickColor()
    # creating the scatter object to return
    lineTrack = go.Scatter(
        x=xData,
        y=yData,
        name=name,
        mode=mode,
        line=dict(
            color=color,
            shape=shape
        )
    )
    return lineTrack


def createDataFill(xData, yData, name):
    """
    Creates a scatter object for filled-line charts
    :param xData: list
    :param yData: list
    :param name: string
    :return: scatter object
    """
    mode = random.choice(['lines', 'none'])
    color = pickColor()
    # creating the scatter object to return
    fillTrack = go.Scatter(
        x=xData,
        y=yData,
        name=name,
        fill='tonexty',
        mode=mode,
        line=dict(
            color=color
        )
    )
    return fillTrack


def createDataDot(xData, yData, name):
    """
    Creates a scatter object for dot charts
    :param xData: list
    :param yData: list
    :param name: string
    :return: scatter object
    """
    symbol = random.choice(['circle','x','diamond-wide','star-diamond-dot'])
    color1 = pickColor()
    color2 = pickColor()

    dotTrack = go.Scatter(
        x=xData,
        y=yData,
        name=name,
        mode='markers',
        marker=dict(
            color=color1,
            line=dict(
                color=color2,
                width=1
            ),
            symbol=symbol
        )
    )
    return dotTrack


def createDataBubble(xData, yData, zData, name):
    """
    Creates a scatter object for bubble charts
    :param xData: list
    :param yData: list
    :param zData: list
    :param name: string
    :return: scatter object
    """
    color = pickColor()
    bubbleTrack = go.Scatter(
        x=xData,
        y=yData,
        name=name,
        mode='markers',
        marker=dict(
            color=color,
            line=dict(
                color='#000',
                width=1
            ),
            size=zData
        )
    )
    return bubbleTrack


def retrieveDataTrack(track, scn, mode, orientation):
    """
    Calculate data from a sample to create traces for chartes
    Call appropriate function depending on the scenario and chart mode indicated
    :param track: integer
    :param scn: string
    :param mode: string
    :param orientation: string
    :return: tuple containing first trace item for data list then the name of current dataset
    """
    databundle = sample[str(track)]
    print("DEBUG : retrieveDataTrack() : databundle = ", databundle)
    xData = databundle['x']
    print("DEBUG : retrieveDataTrack() : xData = ", xData)
    yData = databundle['y']
    print("DEBUG : retrieveDataTrack() : yData = ", yData)
    zData = databundle['z']
    print("DEBUG : retrieveDataTrack() : zData = ", zData)
    trackName = databundle['name']
    print("DEBUG : retrieveDataTrack() : trackName = ", trackName)

    if scn == 'barscn':
        trackData = createDataBar(xData, yData, trackName, orientation)
    elif scn == 'scatscn':
        if mode == 'f':
            trackData = createDataFill(xData, yData, trackName)
        elif mode == 'b':
            trackData = createDataBubble(xData, yData, zData, trackName)
        elif mode == 'l':
            trackData = createDataLine(xData, yData, trackName)
        elif mode == 'd':
            trackData = createDataDot(xData, yData, trackName)
    return trackData, trackName


# ------------------------------------------------------#
#                      BAR SCENARIOS                    #
# ------------------------------------------------------#
def groupLayout(title):
    """
    creates layout object for group style bar layout
    :param title: string
    :return: layout object
    """
    layout = go.Layout(
        barmode='group',
        title=title,
        xaxis=dict(tickangle=-45),
        bargap=0.2,
        bargroupgap=0.1,
        showlegend=True,
        legend=dict(
            orientation='h'
        )
    )
    return layout


def stackLayout(title):
    """
    creates layout object for stack style bar layout
    :param title: string
    :return: layout object
    """
    layout = go.Layout(
        barmode='stack',
        title=title,
        xaxis=dict(tickangle=-45),
        showlegend=True,
        legend=dict(
            orientation='h'
        )
    )
    return layout


def barChart(tracks, rMode):
    """
    Triggers bar type chart scenario with appropriate steps to produce a figure
    :param tracks: integer
    :return: figure object
    """
    data = []
    listname = []
    # Choosing orientation
    rOrientation = random.choice(['h', 'v'])
    print("DEBUG : barChart() : rOrientation = " + rOrientation)

    # Creating each Bar object, appended to data list object
    for track in tracks:
        print("DEBUG : barChart() loop : going to retrieveDataTrack with track, barscn, None and rOrientation in args")
        DATA = retrieveDataTrack(track, 'barscn', None, rOrientation)
        data.append(DATA[0])
        listname.append(DATA[1])
        print("DEBUG : barChart() : DATA in result = ", DATA)
    # Calculating chart title
    title = createTile(listname)
    print("DEBUG : barChart() : title = " + title)

    # Creating Layout object
    if rMode == 'g':
        layout = groupLayout(title)
    if rMode == 's':
        layout = stackLayout(title)

    # Generating the figure to return
    fig = go.Figure(data=data, layout=layout)
    print("DEBUG : barChart() : fig : returning fig")
    print(type(fig))
    return fig


# ------------------------------------------------------#
#                   SCATTER SCENARIOS                   #
# ------------------------------------------------------#

def scatChart(tracks, rMode):
    """
    Triggers scatter type chart scenario with appropriate steps to produce a figure
    :param tracks: integer
    :return: figure object
    """
    # Chosing scatter chart style
    listname = []
    data = []
    # Creating each Bar object, appended to data list object
    for track in tracks:
        print("DEBUG : scatChart() loop : going to retrieveDataTrack with track, scatscn, rMode and None in args")
        trace, tracename = retrieveDataTrack(track, 'scatscn', rMode, None)
        print("DEBUG : scatChart() : DATA[0] = ", trace)
        print("DEBUG : scatChart() : DATA[1] = ", tracename)
        data.append(trace)
        listname.append(tracename)
    # Calculating chart title
    title = createTile(listname)
    print("DEBUG : scatChart() : title = " + title)
    # Creating Layout object
    layout = go.Layout(
        title=title,
        xaxis=dict(
            tickangle=-45,
            showgrid=False,
            showline=True),
        showlegend=True,
        legend=dict(
            orientation='h'
        )
    )
    # Generating the figure to return
    fig = go.Figure(data=data, layout=layout)
    print("DEBUG : scatChart() : fig : returning fig")
    print(type(fig))
    return fig


# ------------------------------------------------------#
#                  HEATMAP SCENARIOS                    #
# ------------------------------------------------------#
def heatmap(track, axis):
    color1 = pickColor()
    color2 = pickColor()
    colorscale = [[0, color1], [1, color2]]
    print("DEBUG : colorscale = ", colorscale)
    tData = sample[str(track)][axis]
    print("DEBUG : tData = ", tData)
    zData = [tData[:5], tData[5:10], tData[10:]] #----------------- ADAPT TO DATASET LENGTH
    print("DEBUG : zData = ", zData)
    title = sample[str(track)]['name']
    print("DEBUG : title = " + title) #--------------------------- MODIFY TITLE CALCULATION

    trace = go.Heatmap(
        z=zData,
        colorscale=colorscale,
        connectgaps=True)
    data = [trace]
    layout = go.Layout(
        title=title
    )

    fig = go.Figure(data=data, layout=layout)
    return fig

#------------------------------------------------------#
#             TRIGER FIG AND CODE CREATION
#------------------------------------------------------#
def createFig(rKey):

    trackid =''

    if rKey == 1 or rKey == 2 :
        rTracks = random.randint(2,5)
        tracks = random.sample(range(1, 9), rTracks)
        print("DEBUG : rTracks = " + str(rTracks))
        print("DEBUG : tracks = ", tracks)
        rMode = random.choice(['g', 's'])
        print("DEBUG : rMode = " + rMode)
        print("DEBUG : barChart() with tracks and rMode in args")
        fig = barChart(tracks, rMode)
        for x in tracks:
            trackid = trackid + str(x)
        code = "b" + rMode + str(rTracks) + trackid
        print("DEBUG : code = " + code)

    elif rKey == 3 or rKey == 4 or rKey == 5:
        rTracks = random.randint(2, 5)
        tracks = random.sample(range(1, 9), rTracks)
        print("DEBUG : rTracks = " + str(rTracks))
        print("DEBUG : tracks = ", tracks)
        rMode = random.choice(['f', 'l', 'd', 'b'])
        print("DEBUG : rMode = " + rMode)
        print("DEBUG : going to scatChart() with tracks and rMode in args")
        fig = scatChart(tracks, rMode)
        for x in tracks:
            trackid = trackid + str(x)
        code = "s" + rMode + str(rTracks) + trackid
        print("DBUG : code = " + code)

    elif rKey == 6:
        rTrack = random.randint(2,9)
        print("DEBUG : rTrack =" + str(rTrack))
        axis = random.choice(['y','z'])
        print("DEBUG : axis =" + str(axis))
        print("DEBUG : going to Heatmap() with rTracks and axis in args")
        fig = heatmap(rTrack, axis)
        code = "h" + axis + str(rTrack)
        print("DEBUG : code = " + code)

    else:
        print("unexpected error, random key must be out of range")

    return fig, code

########################################################
#                        SCRIPT                        #
########################################################
rKey = random.randint(1, 6)
print("DEBUG : rKEy = " + str(rKey))

fig, code = createFig(rKey)

py.image.save_as(fig, filename=code, format='png')