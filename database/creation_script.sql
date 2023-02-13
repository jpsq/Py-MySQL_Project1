create database if not exists python_proyecto1;
--SIEMPRE PARA EVITAR PROBLEMAS EN LOS SCIPTS SQL, LOS COMENTARIOS DEBEN SER LA LINEA EN SI, Y NO EM LA MISMA LINEA DE UN CODIGO

use python_proyecto1;

create table if not exists users(

    users_id int(25) auto_increment not null,
    users_name varchar(100),
    users_surname varchar(150),
    users_email varchar(255) not null,
    users_password varchar(255) not null,
    users_fecha date not null,
    constraint pk_usuarios primary key(users_id),
    constraint uq_email unique(users_email)
    --el email es un campo unico, evitara que en la bd haya 2 usuarios con el mismo email    
)ENGINE=InnoDB;

create table if not exists notes(

    notes_id int(25) auto_increment not null,
    notes_usuarios_id int(25) not null,
    notes_title varchar(255) not null,
    notes_description mediumtext not null,
    --mediumtext es un tipo de dato text pero mayor
    constraint pk_notes primary key(notes_id),
    constraint fk_notes_users FOREIGN KEY(notes_usuarios_id) REFERENCES users(users_id)
)ENGINE=InnoDB;