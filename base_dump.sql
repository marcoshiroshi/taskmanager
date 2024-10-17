SELECT 'Iniciando o processo de inserção de dados adicionais...';

SELECT 'Criando usuários';
INSERT INTO user_user (id, password, last_login, is_superuser, email, first_name, last_name, date_joined, is_active, is_staff) VALUES
(1, 'pbkdf2_sha256$870000$G9KScLpBhmoJEcl3ayt5XQ$H3JbZZXT05PUzDjNOL3gOqz1qicr+7NdbhHdjxITLss=', '2024-10-17 19:56:34.758820', 0, 'marcos.hiroshi99@gmail.com', 'Marcos', 'Hiroshi', '2024-10-17 19:56:28.673346', 1, 0),
(2, 'pbkdf2_sha256$870000$asdfLKJHG90lkjASFhkjl$LKJH0987sdkfjHQ+wehqfkSD345aPoIkj897YwerjjU=', '2024-10-15 12:45:12.123456', 0, 'ana.souza@example.com', 'Ana', 'Souza', '2024-09-10 10:20:15.654321', 1, 1),
(3, 'pbkdf2_sha256$870000$ertKJ987bnlJHYUkJl9kd$98jKLUHYFwer+qwr78nfasfJHI7987hskdjasdasDF=', '2024-10-10 09:10:55.789123', 0, 'paulo.silva@example.com', 'Paulo', 'Silva', '2024-08-25 14:55:23.123456', 1, 0),
(4, 'pbkdf2_sha256$870000$Ytr76sdSDF87gjlUHY89f$j89OIfghSDFGsdfH78JhJLJH90sdj+lkqweO897=', '2024-09-30 18:30:20.987654', 0, 'lucia.almeida@example.com', 'Lúcia', 'Almeida', '2024-07-19 08:45:40.543210', 1, 0),
(5, 'pbkdf2_sha256$870000$jkKl0LKm98JHweUHDssdf$09hweJSDOifkj98jh+sdfLIWER34DSfsdkf897sd=', '2024-09-22 16:55:40.654789', 0, 'carlos.pereira@example.com', 'Carlos', 'Pereira', '2024-06-30 17:35:12.111111', 1, 1),
(6, 'pbkdf2_sha256$870000$dfg0987UJKiytIOWEyrtjs$dfSDfsd8789dfWEwrh34we897hjfOIREkjWEwe43=', '2024-08-20 14:15:33.456789', 0, 'juliana.santos@example.com', 'Juliana', 'Santos', '2024-08-01 19:25:55.789654', 1, 0)
INSERT INTO user_user_groups (id, user_id, group_id) VALUES (1, 1, 1);
INSERT INTO user_user_groups (id, user_id, group_id) VALUES (2, 2, 1);
INSERT INTO user_user_groups (id, user_id, group_id) VALUES (3, 3, 1);
INSERT INTO user_user_groups (id, user_id, group_id) VALUES (4, 4, 1);
INSERT INTO user_user_groups (id, user_id, group_id) VALUES (5, 5, 1);
INSERT INTO user_user_groups (id, user_id, group_id) VALUES (6, 6, 1);

;



SELECT 'Criando tarefas';
INSERT INTO task_task (id, date_create, description, user_id) VALUES
(1, '2024-09-22 14:23:45.123456', 'Criar documentação técnica do projeto', 1),
(2, '2024-10-01 09:10:12.654321', 'Revisar código do módulo de pagamentos', 2),
(3, '2024-08-30 11:45:30.987654', 'Implementar autenticação de dois fatores', 3),
(4, '2024-09-15 16:20:55.555555', 'Desenvolver API REST para integração externa', 1),
(5, '2024-08-28 08:30:01.777777', 'Configurar ambiente de testes automatizados', 2),
(6, '2024-07-25 13:50:45.333333', 'Otimizar consultas ao banco de dados', 3),
(7, '2024-09-07 12:35:40.999999', 'Criar modelo de previsão de vendas com machine learning', 1),
(8, '2024-09-12 10:05:23.111111', 'Implementar sistema de notificação por e-mail', 2),
(9, '2024-09-18 17:47:59.444444', 'Desenvolver interface gráfica para dashboard de vendas', 3),
(10, '2024-08-05 15:25:15.222222', 'Migrar banco de dados de SQLite para PostgreSQL', 1),
(11, '2024-09-01 19:00:55.666666', 'Reestruturar sistema de permissões de usuários', 2),
(12, '2024-07-14 21:17:10.888888', 'Criar relatório gerencial de atividades por usuário', 3),
(13, '2024-08-22 14:05:45.123123', 'Desenvolver sistema de backup automático', 1),
(14, '2024-09-29 07:55:33.555123', 'Criar testes unitários para o módulo de relatórios', 2),
(15, '2024-10-03 18:10:29.777123', 'Implementar integração com gateway de pagamento externo', 3);

SELECT 'Criando registros';
INSERT INTO task_register (id, date_create, task_id, description, minutes) VALUES
(1, '2024-09-22 16:10:30.321654', 4, 'Criação inicial da estrutura de API REST', 240),
(2, '2024-10-01 08:20:45.654789', 5, 'Configuração do Jenkins para testes automatizados', 180),
(3, '2024-08-30 15:35:20.789123', 6, 'Otimização de query SQL no módulo de relatórios', 120),
(4, '2024-09-15 11:40:50.951357', 7, 'Implementação do modelo de machine learning para previsão de vendas', 300),
(5, '2024-08-28 09:25:35.357159', 8, 'Desenvolvimento da funcionalidade de envio de e-mails', 210),
(6, '2024-07-25 16:15:05.753159', 9, 'Desenho e implementação do frontend do dashboard', 360),
(7, '2024-09-07 18:45:10.111222', 10, 'Migração de dados do banco de SQLite para PostgreSQL', 180),
(8, '2024-09-12 10:50:55.543210', 11, 'Refatoração e melhoria no sistema de permissões', 150),
(9, '2024-09-18 17:20:22.876543', 12, 'Geração automática de relatórios com base nas atividades do usuário', 240),
(10, '2024-08-05 12:10:45.654654', 13, 'Implementação de rotinas de backup diárias', 180),
(11, '2024-09-01 14:30:50.258963', 14, 'Desenvolvimento e aplicação de testes unitários', 120),
(12, '2024-07-14 09:20:30.753951', 15, 'Integração da aplicação com o gateway de pagamento', 270),
(13, '2024-08-22 08:45:05.654123', 4, 'Criação da documentação da API REST', 180),
(14, '2024-09-29 19:20:22.321654', 5, 'Melhoria no processo de build automatizado', 150),
(15, '2024-10-03 15:35:40.987111', 6, 'Ajustes na performance das consultas SQL', 200);

SELECT 'Processo finalizado!';