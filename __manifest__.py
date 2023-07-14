{
    'name':'Addon Credito Clientes',
    'version':'1.0',
    'category':'General',
    'summary': '',
    'description': """
    Addon

    Credito a Clientes y Bloquedo


       """,
    'author' : 'M.Gah',
    'website': '',
    'installable': True,
    'auto_install': False,
    'application': True,
    'depends': ['base','sale','account'],
    'data': [
            'security/groups.xml',
            'security/ir.model.access.csv',
            'views/add_credit.xml'
            ],
}
