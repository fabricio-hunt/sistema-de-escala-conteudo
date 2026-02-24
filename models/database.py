"""
Camada de acesso ao banco de dados (Model)
"""
from supabase import create_client, Client
from typing import List, Dict, Optional
import config


class Database:
    """Classe para gerenciar conexões e operações com Supabase"""
    
    def __init__(self):
        """Inicializa a conexão com Supabase"""
        if not config.SUPABASE_KEY:
            raise ValueError("SUPABASE_KEY não configurada. Verifique o arquivo .env")
        
        self.client: Client = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)
    
    # ==================== ESCALAS DE SEXTA-FEIRA ====================
    
    def get_all_escalas(self) -> List[Dict]:
        """Retorna todas as escalas de sexta-feira"""
        try:
            response = self.client.table("escalas_sexta").select("*").order("data", desc=True).execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar escalas: {e}")
            return []
    
    def add_escala(self, nome: str, data: str) -> bool:
        """Adiciona uma nova escala de sexta-feira"""
        try:
            self.client.table("escalas_sexta").insert({
                "nome": nome,
                "data": data
            }).execute()
            return True
        except Exception as e:
            print(f"Erro ao adicionar escala: {e}")
            return False
    
    def update_escala(self, escala_id: int, nome: str, data: str) -> bool:
        """Atualiza uma escala existente"""
        try:
            self.client.table("escalas_sexta").update({
                "nome": nome,
                "data": data
            }).eq("id", escala_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao atualizar escala: {e}")
            return False
    
    def delete_escala(self, escala_id: int) -> bool:
        """Deleta uma escala"""
        try:
            self.client.table("escalas_sexta").delete().eq("id", escala_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao deletar escala: {e}")
            return False
    
    # ==================== FERIADOS ====================
    
    def get_all_feriados(self) -> List[Dict]:
        """Retorna todos os feriados"""
        try:
            response = self.client.table("feriados").select("*").order("data", desc=True).execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar feriados: {e}")
            return []
    
    def add_feriado(self, nome_colaborador: str, nome_feriado: str, data: str, time: str) -> bool:
        """Adiciona um novo feriado"""
        try:
            self.client.table("feriados").insert({
                "nome_colaborador": nome_colaborador,
                "nome_feriado": nome_feriado,
                "data": data,
                "time": time
            }).execute()
            return True
        except Exception as e:
            print(f"Erro ao adicionar feriado: {e}")
            return False
    
    def update_feriado(self, feriado_id: int, nome_colaborador: str, 
                       nome_feriado: str, data: str, time: str) -> bool:
        """Atualiza um feriado existente"""
        try:
            self.client.table("feriados").update({
                "nome_colaborador": nome_colaborador,
                "nome_feriado": nome_feriado,
                "data": data,
                "time": time
            }).eq("id", feriado_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao atualizar feriado: {e}")
            return False
    
    def delete_feriado(self, feriado_id: int) -> bool:
        """Deleta um feriado"""
        try:
            self.client.table("feriados").delete().eq("id", feriado_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao deletar feriado: {e}")
            return False
