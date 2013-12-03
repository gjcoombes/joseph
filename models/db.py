# -*- coding: utf-8 -*-

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate


db = DAL("postgres://postgres:Please123@localhost/joseph",
            pool_size=10,
            check_reserved=['postgres'],)
            # migrate=True, fake_migrate=True, lazy_tables=True)

db.define_table('image',
   Field('title', unique=True),
   Field('file', 'upload'),
   format = '%(title)s')

db.define_table('post',
   Field('image_id', 'reference image'),
   Field('author'),
   Field('email'),
   Field('body', 'text'))


# db.define_table('grids',
#    Field('image_id'),
#    Field('author'),
#    Field('email'),
#    Field('body', 'text'))

db.define_table('simap_grids',
    Field('name', 'string', unique=True),
    Field('description', 'text'),   
    Field('abbreviation', 'string'),
    Field('filename', 'string'),
    Field('source_dirs', 'list:string'),
    Field('sha1', 'string'),
    Field('project', 'string'), 
    Field('origin', 'string'),                        # This will be spatial type Point
    Field('delta',  'string'),                         # This will be spatial type Point
    Field('extent', 'string'),                        # This will be spatial type Polygon
    Field('habitat_id'),                    # This will be a foreign key to habitats.id
    Field('scenario_id'),                   # This will be a foreign key to scenarios.id
    format='%(name)s'
    )




db.image.title.requires = IS_NOT_IN_DB(db, db.image.title)

db.post.image_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')
db.post.author.requires = IS_NOT_EMPTY()
db.post.email.requires = IS_EMAIL()
db.post.body.requires = IS_NOT_EMPTY()
db.post.image_id.writable = db.post.image_id.readable = False


## configure auth policy
auth = Auth(db)
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True