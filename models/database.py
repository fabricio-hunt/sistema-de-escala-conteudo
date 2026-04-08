"""
Camada de acesso ao banco de dados (Model)
"""
from databricks import sql
from typing import List, Dict, Optional
from datetime import date
import config

class Database:
    """Classe para gerenciar conexões e operações com Databricks SQL"""
    
    def __init__(self):
        """Inicializa a configuração com Databricks"""
        if not config.DATABRICKS_TOKEN:
            print("WARNING: DATABRICKS_TOKEN não configurada. Operações de banco poderão falhar.")
            
        self.server_hostname = config.DATABRICKS_SERVER_HOSTNAME
        self.http_path = config.DATABRICKS_HTTP_PATH
        self.access_token = config.DATABRICKS_TOKEN

    def get_connection(self):
        return sql.connect(
            server_hostname=self.server_hostname,
            http_path=self.http_path,
            access_token=self.access_token
        )
    
    # ==================== ESCALAS DE SEXTA-FEIRA ====================
    
    def get_all_escalas(self) -> List[Dict]:
        """Retorna todas as escalas de sexta-feira ordenadas por data ascendente"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id, nome, email, data FROM escalas_sexta ORDER BY data ASC")
                    result = cursor.fetchall()
                    return [{"id": row[0], "nome": row[1], "email": row[2], "data": str(row[3])} for row in result]
        except Exception as e:
            print(f"Erro ao buscar escalas: {e}")
            return []
    
    def delete_past_escalas(self) -> int:
        """Deleta escalas com data anterior a hoje e retorna quantidade deletada"""
        try:
            today_str = date.today().isoformat()
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) as count FROM escalas_sexta WHERE data < :data", {"data": today_str})
                    count_row = cursor.fetchone()
                    count = count_row[0] if count_row else 0
                    
                    if count > 0:
                        cursor.execute("DELETE FROM escalas_sexta WHERE data < :data", {"data": today_str})
                        connection.commit()
                    return count
        except Exception as e:
            print(f"Erro ao deletar escalas passadas: {e}")
            return 0
    
    def add_escala(self, nome: str, email: str, data: str) -> bool:
        """Adiciona uma nova escala de sexta-feira"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO escalas_sexta (nome, email, data) VALUES (:nome, :email, :data)",
                        {"nome": nome, "email": email, "data": data}
                    )
                    connection.commit()
            return True
        except Exception as e:
            import streamlit as st
            st.error(f"Databricks Error (add_escala): {str(e)}")
            print(f"Erro ao adicionar escala: {e}")
            return False
    
    def update_escala(self, escala_id: int, nome: str, email: str, data: str) -> bool:
        """Atualiza uma escala existente"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE escalas_sexta SET nome = :nome, email = :email, data = :data WHERE id = :id",
                        {"nome": nome, "email": email, "data": data, "id": escala_id}
                    )
                    connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar escala: {e}")
            return False
    
    def delete_escala(self, escala_id: int) -> bool:
        """Deleta uma escala"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM escalas_sexta WHERE id = :id", {"id": escala_id})
                    connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar escala: {e}")
            return False
    
    # ==================== FERIADOS ====================
    
    def get_all_feriados(self) -> List[Dict]:
        """Retorna todos os feriados ordenados por data ascendente"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id, nome_colaborador, email, nome_feriado, data, time FROM feriados ORDER BY data ASC")
                    result = cursor.fetchall()
                    return [{
                        "id": row[0], 
                        "nome_colaborador": row[1], 
                        "email": row[2],
                        "nome_feriado": row[3], 
                        "data": str(row[4]), 
                        "time": row[5]
                    } for row in result]
        except Exception as e:
            print(f"Erro ao buscar feriados: {e}")
            return []
    
    def delete_past_feriados(self) -> int:
        """Deleta feriados com data anterior a hoje e retorna quantidade deletada"""
        try:
            today_str = date.today().isoformat()
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) as count FROM feriados WHERE data < :data", {"data": today_str})
                    count_row = cursor.fetchone()
                    count = count_row[0] if count_row else 0
                    
                    if count > 0:
                        cursor.execute("DELETE FROM feriados WHERE data < :data", {"data": today_str})
                        connection.commit()
                    return count
        except Exception as e:
            print(f"Erro ao deletar feriados passados: {e}")
            return 0
    
    def add_feriado(self, nome_colaborador: str, email: str, nome_feriado: str, data: str, time: str) -> bool:
        """Adiciona um novo feriado"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO feriados (nome_colaborador, email, nome_feriado, data, time) VALUES (:nome_colaborador, :email, :nome_feriado, :data, :time)",
                        {"nome_colaborador": nome_colaborador, "email": email, "nome_feriado": nome_feriado, "data": data, "time": time}
                    )
                    connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar feriado: {e}")
            return False
    
    def update_feriado(self, feriado_id: int, nome_colaborador: str, 
                       email: str, nome_feriado: str, data: str, time: str) -> bool:
        """Atualiza um feriado existente"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE feriados SET nome_colaborador = :nome_colaborador, email = :email, nome_feriado = :nome_feriado, data = :data, time = :time WHERE id = :id",
                        {"nome_colaborador": nome_colaborador, "email": email, "nome_feriado": nome_feriado, "data": data, "time": time, "id": feriado_id}
                    )
                    connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar feriado: {e}")
            return False
    
    def delete_feriado(self, feriado_id: int) -> bool:
        """Deleta um feriado"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM feriados WHERE id = :id", {"id": feriado_id})
                    connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar feriado: {e}")
            return False
