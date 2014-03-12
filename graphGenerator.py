'''
Created on Mar 11, 2014

@author: Gustavo Fuentes
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl
import numpy as np

'''
@summary: Metodo que permite crear un grafico y guardarlo en una ruta especificada a partir de los siguientes valores

@param xAxis: valores de eje X 
@param yAxis: valores de eje Y
@param yData: datos de eje Y
@param xData: datos de eje X
@param savePath: ruta completa donde se almacenara el archivo
@param refereceLine: linea referencia
@param xLabel: etiqueta para el eje X //Opcional
@param yLabel: etiqueta para el eje Y //Opcional
@param title: Titulo del grafico //Opcional
@param targetData: etiqueta para los datos de x e y //Opcional
@param prefixYData: prefijo de valores eje X //Opcional
@param prefixXData: prefijo de valores eje Y //Opcional

@type xAxis: list
@type yAxis: list
@type yData: list
@type xData: list
@type yLabel: str
@type xlabel: str
@type title: str
@type referenceLine: Number
@type targetData: str
@type savePath: str
@type prefixYData: str
@type prefixXData: str        
   
'''
def graphGenerator(xAxis,yAxis,xData,yData,savePath,referenceLine,xLabel='No Label',yLabel='No Label',title='No Title',targetData = 'No Target Data',prefixYData='',prefixXData=''):
    
    ###
    referenceLineLegend = 'Reference Line'
    ###
    
    pl.subplot(2,1,1)#division la ventana
    pl.title(title)#set del titulo
    
    #ploteando los datos
    pl.plot(xData, yData, label =  targetData, color='blue', linestyle='--', linewidth=1.0)
    pl.plot(xAxis, [referenceLine for x in xAxis], color = 'red', linestyle = '-', label = referenceLineLegend)
    
    pl.xlabel(xLabel)#set de etiquetas del eje X
    pl.ylabel(yLabel)#set de etiquetas del eje Y
    pl.grid(True)#habilitar red en el mapa cartesiano
    
    pl.xticks(xAxis,[str(y)+str(prefixXData) for y in xAxis], rotation='vertical', style = 'italic',)#set de valores del eje X
    pl.yticks(yAxis,[str(y)+str(prefixYData) for y in yAxis])#set de valores del eje Y
    
    pl.legend(loc='lower center',bbox_to_anchor=(0,-0.7,1,1.3))#set de las legendas
    pl.savefig(savePath,dpi = 200);
    
    
'''
Ejemplo de uso
#llamada al metodo
graphGenerator(range(1,55,3), range(50,100,10),[1,5,20,25,27],[97,94,100,100,99],'/home/gfuentes/migrafico',85.5)
''' 
    
