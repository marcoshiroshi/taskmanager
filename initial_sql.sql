SELECT 'Iniciando o processo de inserção de dados iniciais...';

INSERT INTO auth_group (id, name) VALUES (1, 'USUARIO');
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (1, 1, 32);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (2, 1, 25);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (3, 1, 26);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (4, 1, 27);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (5, 1, 28);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (6, 1, 29);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (7, 1, 30);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (8, 1, 31);

SELECT 'Processo finalizado!';