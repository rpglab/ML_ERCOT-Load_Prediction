# ML_ERCOT-Load_Prediction

Multiple ML models are implemented for ERCOT short-term load forecasting, using weather and time features.

### ML Models:
* Fully-connected neural network (FCNN)
* Support vector machine (SVM)
* Long short-term memory (LSTM)
* Long-term recurrent convolutional network (LRCN)

Multiple variations of the above ML models are trained and evaluated.


### Input Features:
* Weather information
	* temperature
	* long-wave radiation
	* short-wave radiation
	* wind speed
* Time information
	* hour-of-the-day
	* day-of-the-month
	* month-of-the-year


### Data Sources:
Raw ERCOT load data are from ERCOT website: https://www.ercot.com/

Raw weather data are from the Phase 2 of the North American Lan Data Assimilation System (NLDAS-2).

Please refer to the paper below for more details about the data sources.


### Reference:
Initial reference codes: https://rpglab.github.io/resources/ML-Price-Prdctn/


## Citation:
If you use any of our codes/data for your work, please cite the following paper as your reference:

Jonathan Yang, Mingjian Tuo, Jin Lu, and Xingpeng Li, “Analysis of Weather and Time Features in Machine Learning-aided ERCOT Load Forecasting”, *arXiv*, Oct. 2023.

Paper website: https://rpglab.github.io/papers/JonathanY_ML-LF/


## Contributions:
Jonathan developed the codes, trained/evaluated the ML models, and analyzed the results. Mingjian provided guidance for ML structure and helped with code debugging. Jin processed and provided the ERCOT load data and the weather data. Xingpeng supervised this work and analyzed the results. All authors contributed to the paper writing and revisions.


## Contact:
Dr. Xingpeng Li

University of Houston

Email: xli83@central.uh.edu

Website: <a class="off" href="/"  target="_blank">https://rpglab.github.io/</a>


## License:
This work is licensed under the terms of the <a class="off" href="https://creativecommons.org/licenses/by/4.0/"  target="_blank">Creative Commons Attribution 4.0 (CC BY 4.0) license.</a>


## Disclaimer:
The author doesn’t make any warranty for the accuracy, completeness, or usefulness of any information disclosed; and the author assumes no liability or responsibility for any errors or omissions for the information (data/code/results etc) disclosed.

