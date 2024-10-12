class Artista:     
    def __init__(self):         
        self.artistas = []         
        self.genero_musical = 'Pop'   
       
    def agregar_artista(self, artista):         
            self.artistas.append((artista))      
            
    def mostrar_artista(self):         
        genero = self.genero_musical 
        print(genero)     
        for artista in self.artistas:             
            print(f"Artista:",artista)                 
            
    # def buscar_actividad(self, actividad):         
    #     for act, tiempo in self.actividades:             
    #         if act.lower() == actividad.lower():                 
    #             return f"{actividad} se realiza durante {tiempo} horas."         
    #     return f"{actividad} no se encuentra en la rutina."      
        
    # def tiempo_total(self):         
    #         total_horas = sum(tiempo for _, tiempo in self.actividades)         
    #         return f"Tiempo total de actividades: {total_horas} horas."  

artista = Artista() 
artista.agregar_artista('Michael Jackson')   
artista.agregar_artista('Chris Brown')  
artista.agregar_artista('Drake')     
    
print(artista.mostrar_artista()) 
# actividad_buscar = input("Ingrese la actividad que desea buscar: ") 
# resultado = rutina.buscar_actividad(actividad_buscar) 
# print(resultado)  
# print(rutina.tiempo_total())   