# Generated by Django 3.0.2 on 2020-01-30 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='role',
            field=models.CharField(choices=[('Assets', (('parent_asset', 'Asset Account Parent'), ('asset_cash', 'Current Asset'), ('asset_mkt_sec', 'Marketable Securities'), ('asset_liquid', 'Other Liquid Assets'), ('asset_sec', 'Securities'), ('asset_recv', 'Receivables'), ('asset_uncoll', 'Uncollectibles'), ('asset_prepaid', 'Prepaid'), ('asset_inv', 'Inventory'), ('asset_lti', 'Long Term Investments'), ('asset_ppe', 'Property Plant & Equipment'), ('asset_ia', 'Intangible Assets'), ('asset_adj', 'Asset Adjustments'))), ('Liabilities', (('parent_lia', 'Liability Account Parent'), ('lia_cl', 'Current Liabilities'), ('lia_ltl', 'Long Term Liabilities'))), ('Equity', (('parent_cap', 'Capital Account Parent'), ('cap', 'Capital'), ('cap_stock_c', 'Common Stock'), ('cap_stock_p', 'Preferred Stock'), ('cap_adj', 'Capital Adjustments'), ('parent_in', 'Income Account Parent'), ('in_sales', 'Sales Income'), ('in_pass', 'Passive Income'), ('in_other', 'Other Income'), ('parent_cogs', 'COGS Account Parent'), ('ex_cogs', 'Cost of Goods Sold'), ('parent_ex', 'Expense Account Parent'), ('ex', 'Expense'), ('ex_cap', 'Capital Expense'), ('ex_other', 'Other Expense')))], max_length=15, verbose_name='Account Role'),
        ),
    ]
