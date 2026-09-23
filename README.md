# Ember Network Analysis — Scotland

## Overview

This project maps Ember's current network of 19 electric coach routes against Scottish population density, using timetable data from the UK Bus Open Data Service and small area population estimates from National Records of Scotland.

The interactive map shows Ember's routes and stops overlaid on a population heatmap, making it easy to see where Ember currently operates and where significant populations remain unserved.

[View the interactive map](https://jo-malo.github.io/ember-network-analysis/ember_network.html)

## What the map shows

Ember's current network connects Scotland's major cities well: Edinburgh, Glasgow, Dundee, Aberdeen, Inverness and Fort William are all served, with good coverage of the central belt corridor. Stirling and Falkirk are served as stops on existing routes.

Two gaps stand out when population density is overlaid:

### 1. The Ayrshire coast: Glasgow to Ayr via Kilmarnock, Irvine and Saltcoats

The Ayrshire coast represents one of the most densely populated unserved corridors in Scotland. Kilmarnock (46,000), Irvine (33,000), Saltcoats and Ayr (47,000) form a continuous population corridor south of Glasgow with strong existing travel demand evidenced by ScotRail usage on the same corridor.

An Ember route connecting Glasgow to Ayr, stopping at Kilmarnock, Irvine and Saltcoats would serve a combined catchment population of over 150,000 people currently without an intercity electric coach option. Journey times would be competitive with rail on this corridor, and the charging infrastructure requirements are manageable given the proximity to Glasgow.

### 2. Motherwell and Hamilton: South Lanarkshire's missing link

Motherwell and Hamilton together have a population of over 80,000 and sit just south of Glasgow, yet neither is currently served by Ember. Both towns have strong commuter and leisure travel patterns toward Glasgow and Edinburgh.

Rather than a standalone route, Motherwell and Hamilton could be incorporated as stops on a future Glasgow to Edinburgh via South Lanarkshire service, offering an alternative corridor to the existing E3 and capturing demand from one of Scotland's most densely populated unserved areas.

## Methodology

- **Route and stop data:** UK Bus Open Data Service (GTFS format), filtered to Ember operator code OP965
- **Population data:** National Records of Scotland Small Area Population Estimates 2024, Data Zone Centroids 2022
- **Tools:** Python, Pandas, GeoPandas, Folium
- **Map:** Interactive HTML, hosted on GitHub Pages

## Data sources

- [UK Bus Open Data Service](https://data.bus-data.dft.gov.uk)
- [National Records of Scotland](https://www.nrscotland.gov.uk)
- [Scottish Government Data Zone Centroids 2022](https://www.data.gov.uk/dataset/d5b6fbc1-8a79-46c6-ac64-2de60c6fcb70/data-zone-centroids-2022)