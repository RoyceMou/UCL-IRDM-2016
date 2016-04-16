require(forecast)
data<-read.csv(file.choose(),header=T)
attach(data)

rmse=c()
for(i in 1:20){
  zone1=data[which(zone_id==i),]
  load1=zone1[,6]
  load1=load1[-which(is.na(load1)==T)]
  tsload1<-ts(load1,start = c(2004,1),frequency = 8766)
  #training data
  tsload1train=tsload1[1:(length(tsload1)-186)]
  #test data
  tsload1test=tsload1[(length(tsload1)-186+1):length(tsload1)]
  #Identification of best fit ARIMA model
  arima1 <- auto.arima(tsload1train, approximation=FALSE,trace=FALSE)
  #Forecast using the best fit ARIMA model
  forecast1=forecast(arima1,h=186)$mean
  forecast1=as.numeric(forecast1)
  rmse[i]=sqrt(sum((tsload1test-forecast1)^2)/186)
}

