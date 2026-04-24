## Introduction

Traffic, industrial pollution, and wildfires have subjected the Los Angeles metropolitan area to adverse air quality for decades. Such environmental conditions expose residents to increased risk of health problems, exacerbated allergic reactions, and physiological interruptions to daily life. A recent California Air Resources Board study estimated that particulate pollution causes over 9,000 deaths in California annually (LA County Public Health).

As climate change and industrial activity continue to compound the worsening levels of air pollution, improved technology may help to predict adverse air quality events. A machine learning (ML) architecture designed for this task may be most appropriate as mathematical models require updates to remain accurate. If effective, a predictive ML model will inform county and state health departments as they disseminate warnings to stay indoors, wear masks, and utilize air filtration where possible. 

Air quality is typically measured by metrics such as the Air Quality Index (AQI), which factors in pollutants like O3, NO2, CO, sulfates, nitrates, and black carbon. In a study by Liu et al. (2009), exposure to an average SO2 concentration of 5.0 ppb across a two-day window elicited adverse effects in children (aged 9-14) with asthma. In the event of an asthma reaction, symptoms can include bronchoconstriction and restricted lung function (US EPA, 2018). Concentrations higher than that (~500-2000 ppb) could cause similar effects in patients with mild asthma or who are healthy (Liu et al., 2009). 

The target variable we measured was the concentration of each pollutant, namely PM 2.5. We aimed to achieve a root mean squared error (RMSE) of less than 3. The model predicts PM 2.5 in hourly intervals, over 24 hours (1 day) or 172 hours (1 week). While the model predicts air quality at specific sensor sites, we envision the development of an interpolation model to output an air quality prediction at any latitude and longitude.

Another project objective was to embed the model into a user-facing application. The ultimate motivation for this project was to inform people with respiratory conditions about upcoming air quality. Users of our envisioned application can visualize the levels of air quality by US EPA published levels of severity (Figure 1).

<div align="center">
  <img width="404" height="305" src="https://github.com/user-attachments/assets/55073f7d-c431-4b9f-a743-19ae6e3064f9" alt="AA_fig1" />
  <p><b>Figure 1.</b> Air Quality Index (AQI) and PM 2.5 levels of health concern (EPA, 2025).</p>
</div>

We first designed a GNN-LSTM model to predict PM 2.5 in the Hawaiian islands. Due to its remote location and relative lack of anthropogenic air pollution, Hawaii faces mainly natural disasters, including wildfires and volcanic eruptions, as causes of adverse air quality. This made it a simple region to refine and test our model. In the 2024-2025 cycle, we applied this GNN-LSTM architecture to the greater Los Angeles area, a region with many nonpoint sources of air pollution. This more difficult task required our model to develop a greater understanding of air pollution movement over space and time.

Previous studies have examined air quality post-disaster in metropolitan areas. However, the implementation of machine learning predictions of LA air quality by the LA County Department of Public Health is not evident. In addition, predictions of air quality extended just 72 hours into the future. Building off of our work on Hawaii air quality, we aimed to fit our model to the conditions of Los Angeles and also predict air quality a week into the future. With the completion of these tasks, our predictive model is generally useful for users across the Los Angeles metropolitan area and applicable to other urban centers.

This project primarily addressed the Grand Challenge Themes of Sustainability and Health. The air quality monitoring will promote greater attention on the environment and can be used by all to identify good days for low- and high-intensity outdoor activities. With the assistance of this project’s application, these outdoor activities will foster greater human health. Especially for patients with asthma or other respiratory conditions, this project may allow individuals to enjoy the outdoors without fear of adverse respiratory effects. In doing so, this project also addresses the Grand Challenge Theme of the Joy of Living. The ultimate goal was to aid an overlooked population that will benefit from healthier, more environmentally-conscious lifestyles.

## Methods

<div align="center">
  
<table>
  <tr>
    <th align="center">OpenAQ</th>
    <th align="center">OpenMeteo</th>
  </tr>
  <tr>
    <td align="center">PM 1 (µg/m³)</td>
    <td align="center">Temperature</td>
  </tr>
  <tr>
    <td align="center">PM 1 (particles/cm³)</td>
    <td align="center">Relative Humidity</td>
  </tr>
  <tr>
    <td align="center">PM 2.5 (µg/m³)</td>
    <td align="center">Dew Point</td>
  </tr>
  <tr>
    <td align="center">PM 2.5 (particles/cm³)</td>
    <td align="center">Apparent temperature</td>
  </tr>
  <tr>
    <td align="center">PM 10 (µg/m³)</td>
    <td align="center">Precipitation</td>
  </tr>
  <tr>
    <td align="center">PM 10 (particles/cm³)</td>
    <td align="center">Surface Pressure</td>
  </tr>
  <tr>
    <td align="center">SO<sub>2</sub> (ppm)</td>
    <td align="center">Cloud cover</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td align="center">Wind speed 10m</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td align="center">Wind direction 10m</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td align="center">Wind speed 100m</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td align="center">Wind direction 100m</td>
  </tr>
  <tr>
    <td align="center"></td>
    <td align="center">Soil temperature</td>
  </tr>
</table>

<p align="center"><b>Table 1.</b> Features gathered from OpenAQ and OpenMeteo databases.</p>

</div>

Air quality and weather data in the Greater Los Angeles area were gathered using the OpenAQ and OpenMeteo APIs, respectively. Data was collected from over 200 sensor locations in the year 2023, the first year with adequate PurpleAir sensor coverage.
To train a machine learning model on this Los Angeles dataset, we utilized the GNN-LSTM architecture that we first investigated in the 2023-2024 fellowship year in the Hawaii dataset. The GNN-LSTM architecture uses a graph neural network (GNNs) to represent the location and distances between sensor sites and links each hour of data through a temporal model such as a long short-term model (LSTM). This architecture has been used in related research to model wildfire-related smoke movements in California (Liao et al. 2023).

<div align="center">
  <img width="590" height="250" src="https://github.com/user-attachments/assets/815e79fe-2399-4202-80ef-0c501dd5fc58" alt="AA_fig1" />
  <p><b>Figure 2.</b> From Bronstein (2020). A depiction of a temporal graph neural network. A graph represents data from each time point, and each graph is connected temporally to the data before and after it.</p>
</div>

Apart from the switch to the Los Angeles data source, we made several optimizations to the GNN-LSTM model this fellowship year. Firstly, we simplified the architecture, which increased gradient propagation and lowered training times. Additionally, we applied Gaussian normalization to all input data to reduce the importance of feature ranges. We expanded our model from predicting just the next hour based on the previous day to predicting the next 24 hours, which improved model performance through increased generalizability. We took this further by predicting a whole week in advance based on the previous week. This allows for greater usability by people with respiratory conditions to plan out their weekly activities to avoid days with adverse air quality.

Commercially available Large Language Models (LLMs) aided in debugging and data cleaning. Most utilized were Claude 3.5 Sonnet, OpenAI GPT-4o, and DeepSeek V3-0324. LLM helpfulness was comparable between companies; however, ‘reasoning’ modes produced more helpful answers. Model outputs were almost never error-free, so it is likely that general familiarity with the Python language and PyTorch packages was necessary to refine the code to produce an effective GNN-LSTM model.

## Results

<div align="center">

<table>
  <tr>
    <th align="center">Architecture</th>
    <th align="center">RMSE</th>
  </tr>
  <tr>
    <td align="center">Initial GNN-LSTM</td>
    <td align="center">25.24</td>
  </tr>
  <tr>
    <td align="center">Optimized GNN-LSTM</td>
    <td align="center">19.46</td>
  </tr>
  <tr>
    <td align="center">GNN-LSTM with normalization (predicts next hour)</td>
    <td align="center">2.26</td>
  </tr>
  <tr>
    <td align="center">GNN-LSTM with normalization (predicts next 24 hours)</td>
    <td align="center">1.41</td>
  </tr>
  <tr>
    <td align="center">GNN-LSTM with normalization (predicts next week)</td>
    <td align="center">2.00</td>
  </tr>
</table>

<p align="center"><b>Table 2.</b> RMSE of various GNN-LSTM model architectures over the Los Angeles area in 2023.</p>

</div>

Applying various optimizations to our GNN-LSTM model resulted in a great reduction in RMSE throughout the year on the Los Angeles dataset. Compared to the initial RMSE of 25.24, the final 24-hour prediction model had an RMSE of 1.41, a 95% reduction in error. Even though predicting air quality one week in the future is a much more difficult task than 24 hours, the one-week model still produces a comparatively low RMSE of 2.00, showcasing the robustness of the GNN-LSTM model architecture.

<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <td style="width: 32%; padding: 2px;"><img src="https://github.com/user-attachments/assets/b3d957c8-ccbf-4ac2-8020-c534b254bb4a" alt="image5" width="100%"/></td>
    <td style="width: 32%; padding: 2px;"><img src="https://github.com/user-attachments/assets/0102a5df-fce6-4465-8108-b65cc476798e" alt="image9" width="100%"/></td>
    <td style="width: 32%; padding: 2px;"><img src="https://github.com/user-attachments/assets/de884264-949b-47e9-a3c7-ac1e34090d3b" alt="image8" width="100%"/></td>
  </tr>
</table>
<p align="center"><b>Figure 3.</b> Target (top) vs Output (bottom) distribution comparison for 1-hour (left), 24-hour (middle), and 172-hour (right) models.</p>

<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <td style="width: 32%; padding: 2px;"><img src="https://github.com/user-attachments/assets/0d549cfb-2c8c-4029-b618-2f6aab1ba9fe" alt="image3" width="100%"/></td>
    <td style="width: 32%; padding: 2px;"><img src="https://github.com/user-attachments/assets/160cfe6b-aa75-41e8-8145-6d3adc6bc62e" alt="image2" width="100%"/></td>
    <td style="width: 32%; padding: 2px;"><img src="https://github.com/user-attachments/assets/1f6e9302-0044-4cbc-b1db-8925da83b999" alt="image6" width="100%"/></td>
  </tr>
</table>
<p align="center"><b>Figure 4.</b> Train-test RMSE plots over model training for 1-hour (left), 24-hour (middle), and 172-hour (right) models.</p>

While all models had similar target-output comparisons, the train-test plots showed significant variation. The 1-hour plot had a reduction in train loss but with a stagnant test loss, indicating overfitting. In contrast, the 24-hour plot shows a reduction in both train and test loss with the beginning of a level off after around 200 epochs. This indicates a model that has learned the training data well, with generalization ability to the test set. 

The 172-hour (1-week) model also shows a reduction in both train and test loss over the training epochs. However, there is no level off or separation between train and test loss. This is due to the fact that training the 1-week model required significantly higher GPU resources and slower training time, limiting the amount of training we could do on USC’s High-Performance Computing (HPC) clusters. Because of this, the model was limited to 1000 epochs of training. However, with more GPU time and resources, we expect the model to continue its improvement.

After the training of performant models, we shifted to developing a prototype application. This application would display air quality predictions from the 1-week model at a selected date and time. Users are able to view all the sensors in the LA area and find the air quality predictions at their closest sensors over the forecast period. Additionally, sensors are colored according to the EPA’s air quality warning scale (Figure 1) so users can easily identify areas of severe air quality. This prototype application can be accessed at https://alohaair.streamlit.app/

<div align="center">
  <img width="1052" height="749" src="https://github.com/user-attachments/assets/e11448d0-d7da-40bf-a27d-a85371217463" alt="AA_fig1" />
  <p><b>Figure 5.</b> Screenshot from prototype application showing air quality predictions in the LA area with color corresponding to air quality severity.</p>
</div>

Future work should expand this application to real-time air quality prediction, with the app gathering the past week of sensor data and passing that into an online GNN-LSTM model endpoint. The web application should also feature specific warnings and notifications for highly sensitive groups, such as those with respiratory conditions. Additionally, improving model performance is always an area of exploration, whether through increasing training data or improving the model architecture. The transformer architecture, in particular, may provide an increase in performance due to the attention mechanism that uniquely learns long-range dependencies in temporal data. The transformer also has lower training times than the LSTM, which is crucial when training 1-week or longer time-scale models.

Further efforts should also market this model to health systems (such as Kaiser Permanente) and the Los Angeles Department of Public Health. In our attempt of this outreach, the reception was positive but non-committal. We still believe that partnering with a large system would be the most efficient course of action.

## References

* Bronstein M. (2020). **Temporal Graph Networks**. *Towards Data Science*. [https://towardsdatascience.com/temporal-graph-networks-ab8f327f2efe](https://towardsdatascience.com/temporal-graph-networks-ab8f327f2efe)

* Liao, K., Buch, J., Lamb, K., & Gentine, P. (2023). **Simulating the Air Quality Impact of Prescribed Fires Using Graph Neural Network-Based PM2.5 Forecasts**. [https://arxiv.org/abs/2312.04291](https://arxiv.org/abs/2312.04291)

* Liu, L., Poon, R., Chen, L., Frescura, A. M., Montuschi, P., Ciabattoni, G., Wheeler, A., & Dales, R. (2009). **Acute effects of air pollution on pulmonary function, airway inflammation, and oxidative stress in asthmatic children**. *Environmental Health Perspectives*, 117(4), 668–674. [https://doi.org/10.1289/ehp11813](https://doi.org/10.1289/ehp11813)

* Los Angeles County Public Health Department. **Criteria Air Pollutants: Los Angeles County**. *L.A. County Department of Public Health*. [http://publichealth.lacounty.gov/eh/safety/criteria-air-pollutants.htm](http://publichealth.lacounty.gov/eh/safety/criteria-air-pollutants.htm)

* OpenAQ, Inc. (2024). **OpenAQ API**. Available from: [https://openaq.org](https://openaq.org)

* US EPA. (2018). **Risk and exposure assessment for the review of the primary national ambient air quality standard for sulfur oxides**. *EPA-452/R-18-003*.

* U.S. Environmental Protection Agency. (2025). **Patient Exposure and the Air Quality Index**. In *Ozone Pollution and Your Patients’ Health*. [https://www.epa.gov/ozone-pollution-and-your-patients-health/patient-exposure-and-air-quality-index](https://www.epa.gov/ozone-pollution-and-your-patients-health/patient-exposure-and-air-quality-index)

* Zippenfenig, P. (2023). **Open-Meteo.com Weather API** [Computer software]. *Zenodo*. [https://doi.org/10.5281/ZENODO.7970649](https://doi.org/10.5281/ZENODO.7970649)
