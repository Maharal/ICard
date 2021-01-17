CREATE TABLE User (
   id                  INT PRIMARY KEY NOT NULL,
   photo_url           TEXT,
   birth_day           DATE,
   profession          TEXT,
   profile_description TEXT,
   country             TEXT,
   state               TEXT,
   city                TEXT,
   creation_date       DATE NOT NULL DEFAULT CURRENT_DATE,
   update_date         DATE NOT NULL
);


CREATE TABLE Card (
   id                  INT PRIMARY KEY NOT NULL,
   id_user             INT NOT NULL,
   title               TEXT,
   card_description    TEXT,
   creation_date       DATE NOT NULL DEFAULT CURRENT_DATE,
   update_date         DATE NOT NULL,    
   CONSTRAINT fk_owner_user
      FOREIGN KEY (id_user) 
	  REFERENCES User(id)
);


CREATE TABLE favorite (
    id                  INT PRIMARY KEY NOT NULL,
    id_user             INT NOT NULL, 
   creation_date       DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT fk_favorite_user
      FOREIGN KEY (id_user) 
	  REFERENCES User(id)
);