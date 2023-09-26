# Exploring U.S. National-Parks: Visitor and Accommodation Trends
This project explores visitor and accommodation trends across U.S. national parks, utilizing data from various sources.

## Tableau Workbook (Story)
The Tableau workbook [NationalParks.twb](https://github.com/etsar/Exploring-U.S.-National-Parks/blob/main/NationalParks.twb) serves as the central hub for visualizing and analyzing data related to national park visitation and overnight stays. The workbook is organized into multiple tabs (story points), each offering unique perspectives on the data. You can also [view the Tableau Story online](https://public.tableau.com/views/ExploringU_S_NationalParksVisitorandAccommodationTrends/ExploringU_S_NationalParksVisitorandAccommodationTrends?:language=en-US&:display_count=n&:origin=viz_share_link) to interact with the visualizations and explore the data further.

### Visitor Overview
<table>
  <tr>
    <td width="55%">
      <ul>
        <li><b>Total Visitors</b>: A dynamic summary view displaying the total number of visitors based on user selections, including the chosen time period, national park(s), and visitor type (Recreation, Non-Recreation). This view adapts to various filter combinations, providing insights into visitor statistics tailored to your preferences.</li>
        <li><b>Visitors Over the Years</b>: A dynamic line chart illustrating trends in visitors over the years, with separate lines for recreation and non-recreation visitors. This chart adapts to user selections, allowing to focus on the specific national park(s) by selecting them on the "Visitors by Park and Type" chart.</li>
        <li><b>Distribution of Visitors by Type</b>: A dynamic pie chart showcasing the distribution of visitors by type based on user selections for the time period and national park(s).</li>
        <li><b>Visitors by Park and Type</b>: A dynamic horizontal bar chart detailing the number of visitors by national park and type for the selected period.</li>
        <li><b>Recreation Visitors by Month</b>: A dynamic line chart depicting monthly trends in recreation visitors for selected year(s) and national park(s).</li>
      </ul>
    </td>
    <td width="45%" align="center">
      <img src="https://github.com/etsar/Exploring-U.S.-National-Parks/assets/94500188/41c89092-ce8d-4ab3-906e-75120e862982" alt="Visitor Overview" width="400" height="350">
    </td>
  </tr>
</table>


### Overnight Stays
<table>
  <tr>
    <td width="55%">
      <ul>
        <li><b>Total Overnight Stays</b>: A dynamic summary view displaying the total number of overnight stays based on user selections, including the chosen time period and national park(s).</li>
        <li><b>Overnight Stays Over the Years</b>: A dynamic line chart illustrating trends in overnight stays over the years, segmented by accommodation type. This chart adapts to user selections, allowing to focus on the specific national park(s) by selecting them on the "Overnight Stays by Park and Type" chart.</li>
        <li><b>Distribution of Overnight Stays by Type</b>: A dynamic pie chart showcasing the breakdown of overnight stays by accommodation type based on user selections for the time period and national park(s).</li>
        <li><b>Overnight Stays by Park and Type</b>: A dynamic horizontal bar chart detailing the number of overnight stays by national park and accommodation type for the selected period.</li>
        <li><b>Overnight Stays by Month</b>: A dynamic vertical bar chart depicting monthly trends in overnight stays for selected year(s) and national park(s), categorized by accommodation type.</li>
      </ul>
    </td>
    <td width="45%" align="center">
      <img src="https://github.com/etsar/Exploring-U.S.-National-Parks/assets/94500188/7985aa77-86a9-4609-936d-fb03cc88181f" alt="Overnight Stays" width="400" height="350">
    </td>
  </tr>
</table>

### Park Location and Visitor Density
<table>
  <tr>
    <td width="55%">
      <p><b>Park Location Map by Number of Visitors and Park Area</b>: An interactive map featuring national park locations. Dot size represents the number of recreation visitors, while dot color corresponds to park area. Hover over dots for detailed information about each park.
      </p>
    </td>
    <td width="45%" align="center">
      <img src="https://github.com/etsar/Exploring-U.S.-National-Parks/assets/94500188/59164c09-3ebd-4925-810f-ca910e97a7a8" alt="Park Location and Visitor Density" width="400" height="350">
    </td>
  </tr>
</table>


### Data Sources and Definitions
In this section, you can access key resources and documentation related to data sources and data processing.
- <b>Data Sources</b>: Find links to the data sources used in this project, including the National Park Service Visitor Use Statistics (irma.nps.gov) and Wikipedia. These sources provide crucial information for understanding the context of the analysis.
- <b>Scripts for Data Retrieval</b>: Explore Python scripts [get_stats_xlsx.py](https://github.com/etsar/Exploring-U.S.-National-Parks/blob/main/get_stats_xlsx.py) and [get_stats_wiki_xlsx.py](https://github.com/etsar/Exploring-U.S.-National-Parks/blob/main/get_stats_wiki_xlsx.py) used to automate the retrieval of data from irma.nps.gov and Wikipedia.
- <b>Data Preprocessing Notebook</b>: Dive into the Jupyter Notebook [national_park_data_preprocessing.ipynb](https://github.com/etsar/Exploring-U.S.-National-Parks/blob/main/national_park_data_preprocessing.ipynb) that documents the data preprocessing steps. This notebook outlines how downloaded reports from irma.nps.gov are combined into a unified dataset, and how data cleaning and formatting are performed to prepare the data for analysis.
- <b>Definitions</b>: Understand key terms used in this project, such as "Non-Recreation Visit", "Overnight Stay", and the six categories that classify types of overnight stays.
