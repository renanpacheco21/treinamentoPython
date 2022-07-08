from funcoes import executar, consultar, permissao

resultado = consultar("""
                select 
                i_pessoas as pessoa, 
                email
                from bethadba.pessoas
                //where email is null
                where email is not null
                and bethadba.dbf_valida_email(trim(email)) = 1
                """)
print(resultado)

for i in resultado:
    executar(permissao(f"""
            update bethadba.pessoas
            set email = null
            where i_pessoas = {i['pessoa']};
            """))
    print(i)
