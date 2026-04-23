Introduction

Facing the effects of traffic, industrial pollution, and wildfires, the Los Angeles metropolitan area has been plagued by adverse air quality for decades. Such environmental conditions expose residents to increased risk of health problems, exacerbated allergic reactions, and physiological interruptions to daily life. A recent California Air Resources Board study estimated that particulate pollution causes over 9,000 deaths in California annually (LA County Public Health).

As climate change and industrial activity continue to compound the worsening levels of air pollution, improved technology may help to predict adverse air quality events. A machine learning (ML) architecture designed for this task may be most appropriate as mathematical models require updates to remain accurate. If effective, a predictive ML model will inform county and state health departments as they disseminate warnings to stay indoors, wear masks, and utilize air filtration where possible. 

Air quality is typically measured by metrics such as the Air Quality Index (AQI), which factors in pollutants like O3, NO2, CO, sulfates, nitrates, and black carbon. In a study by Liu et al. (2009), exposure to an average SO2 concentration of 5.0 ppb across a two-day window elicited adverse effects in children (aged 9-14) with asthma. In the event of an asthma reaction, symptoms can include bronchoconstriction and restricted lung function (US EPA, 2018). Concentrations higher than that (~500-2000 ppb) could cause similar effects in patients with mild asthma or who are healthy (Liu et al., 2009). 

The target variable we measured was the concentration of each pollutant, namely PM 2.5. We aimed to achieve a root mean squared error (RMSE) of less than 3. The model predicts PM 2.5 in hourly intervals, over 24 hours (1 day) or 172 hours (1 week). While the model predicts air quality at specific sensor sites, we envision the development of an interpolation model to output an air quality prediction at any latitude and longitude.

Another project objective was to embed the model into a user-facing application. The ultimate motivation for this project was to inform people with respiratory conditions about upcoming air quality. Users of our envisioned application can visualize the levels of air quality by US EPA published levels of severity (Figure 1).
<img width="1616" height="1220" alt="AA_fig1" src="https://github.com/user-attachments/assets/55073f7d-c431-4b9f-a743-19ae6e3064f9" />

Figure 1. Air Quality Index (AQI) and PM 2.5 levels of health concern (EPA, 2025).








In the 2023-2024 fellowship cycle, we designed a GNN-LSTM model to predict PM 2.5 in the Hawaiian islands. Due to its remote location and relative lack of anthropogenic air pollution, Hawaii faces mainly natural disasters, including wildfires and volcanic eruptions, as causes of adverse air quality. This made it a simple region to refine and test our model. In the 2024-2025 cycle, we applied this GNN-LSTM architecture to the greater Los Angeles area, a region with many nonpoint sources of air pollution. This more difficult task required our model to develop a greater understanding of air pollution movement over space and time.

Previous studies have examined air quality post-disaster in metropolitan areas. However, the implementation of machine learning predictions of LA air quality by the LA County Department of Public Health is not evident. In addition, predictions of air quality extended just 72 hours into the future. Building off of our work on Hawaii air quality, we aimed to fit our model to the conditions of Los Angeles and also predict air quality a week into the future. With the completion of these tasks, our predictive model is generally useful for users across the Los Angeles metropolitan area and applicable to other urban centers.

This project primarily addressed the Grand Challenge Themes of Sustainability and Health. The air quality monitoring will promote greater attention on the environment and can be used by all to identify good days for low- and high-intensity outdoor activities. With the assistance of this project’s application, these outdoor activities will foster greater human health. Especially for patients with asthma or other respiratory conditions, this project may allow individuals to enjoy the outdoors without fear of adverse respiratory effects. In doing so, this project also addresses the Grand Challenge Theme of the Joy of Living. The ultimate goal was to aid an overlooked population that will benefit from healthier, more environmentally-conscious lifestyles.
