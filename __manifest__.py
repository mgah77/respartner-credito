{
    'name':'Addon Credito Clientes',
    'version':'2.0.2',
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
    'depends': ['base','sale','account','l10n_cl_fe'],
    'data': [
            'security/groups.xml',
            'security/ir.model.access.csv',
            'views/add_credit.xml'
            ],
}
