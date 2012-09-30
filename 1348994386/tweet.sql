DROP   TABLE IF     EXISTS tweet;
CREATE TABLE IF NOT EXISTS tweet (
    tid  INT(10)       AUTO_INCREMENT,
    body VARCHAR(255),
    PRIMARY KEY (tid)
)Engine=InnoDB;
