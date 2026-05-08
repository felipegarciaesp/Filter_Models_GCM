# CODIGO PARA FILTRAR MODELOS GCM, creado por Felipe Garcia
# 
# 
# Cuando se trabaja con modelos de cambio climático, hay necesidad de eliminar modelos que no se ajusten a ciertos criterios.
# Este codigo entregará un vector con los modelos seleccionados.
# 

## Carga de librerias
import pandas as pd 
import numpy as np

## Cargar planilla, asignar modelos originales y por eliminar
GCM_initials = pd.read_excel("GCMs.xlsx", sheet_name="Initial").drop_duplicates().reset_index(drop=True)
GCM_eliminated = pd.read_excel("GCMs.xlsx", sheet_name="Eliminated").drop_duplicates().reset_index(drop=True)

# DataFrame con datos filtrados:
GCM_filtrated = GCM_initials[~GCM_initials['Models'].isin(GCM_eliminated['Models'])].reset_index(drop=True)

# Exportar a Excel sin el indice:
GCM_filtrated.to_excel("GCMs_filtrated.xlsx", index=False)
