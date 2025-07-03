# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllFuelsData(models.Model):
    ticker = models.TextField(blank=True, null=True)
    commodity = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_fuels_data'


class Annotations(models.Model):
    image_id = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    bounds = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annotations'


class Brentoilprices(models.Model):
    date = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brentoilprices'


class CrudeOilPrice(models.Model):
    date = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    percentchange = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crude_oil_price'


class CrudeOilPrices(models.Model):
    entity = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    oil_price_crude_prices_since_1861_current_us_field = models.FloatField(db_column='oil_price___crude_prices_since_1861_(current_us$)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'crude_oil_prices'


class Data(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    originname = models.TextField(blank=True, null=True)
    origintypename = models.TextField(blank=True, null=True)
    destinationname = models.TextField(blank=True, null=True)
    destinationtypename = models.TextField(blank=True, null=True)
    gradename = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    origin_lat = models.FloatField(blank=True, null=True)
    origin_lon = models.FloatField(blank=True, null=True)
    dest_lat = models.FloatField(blank=True, null=True)
    dest_lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'


class Database(models.Model):
    report_number = models.IntegerField(blank=True, null=True)
    supplemental_number = models.IntegerField(blank=True, null=True)
    accident_year = models.IntegerField(blank=True, null=True)
    accident_date_time = models.TextField(db_column='accident_date/time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    operator_id = models.IntegerField(blank=True, null=True)
    operator_name = models.TextField(blank=True, null=True)
    pipeline_facility_name = models.TextField(db_column='pipeline/facility_name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pipeline_location = models.TextField(blank=True, null=True)
    pipeline_type = models.TextField(blank=True, null=True)
    liquid_type = models.TextField(blank=True, null=True)
    liquid_subtype = models.TextField(blank=True, null=True)
    liquid_name = models.TextField(blank=True, null=True)
    accident_city = models.TextField(blank=True, null=True)
    accident_county = models.TextField(blank=True, null=True)
    accident_state = models.TextField(blank=True, null=True)
    accident_latitude = models.FloatField(blank=True, null=True)
    accident_longitude = models.FloatField(blank=True, null=True)
    cause_category = models.TextField(blank=True, null=True)
    cause_subcategory = models.TextField(blank=True, null=True)
    unintentional_release_barrels_field = models.FloatField(db_column='unintentional_release_(barrels)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    intentional_release_barrels_field = models.FloatField(db_column='intentional_release_(barrels)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    liquid_recovery_barrels_field = models.FloatField(db_column='liquid_recovery_(barrels)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    net_loss_barrels_field = models.FloatField(db_column='net_loss_(barrels)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    liquid_ignition = models.TextField(blank=True, null=True)
    liquid_explosion = models.TextField(blank=True, null=True)
    pipeline_shutdown = models.TextField(blank=True, null=True)
    shutdown_date_time = models.TextField(db_column='shutdown_date/time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    restart_date_time = models.TextField(db_column='restart_date/time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    public_evacuations = models.FloatField(blank=True, null=True)
    operator_employee_injuries = models.FloatField(blank=True, null=True)
    operator_contractor_injuries = models.FloatField(blank=True, null=True)
    emergency_responder_injuries = models.FloatField(blank=True, null=True)
    other_injuries = models.FloatField(blank=True, null=True)
    public_injuries = models.FloatField(blank=True, null=True)
    all_injuries = models.FloatField(blank=True, null=True)
    operator_employee_fatalities = models.FloatField(blank=True, null=True)
    operator_contractor_fatalities = models.FloatField(blank=True, null=True)
    emergency_responder_fatalities = models.FloatField(blank=True, null=True)
    other_fatalities = models.FloatField(blank=True, null=True)
    public_fatalities = models.FloatField(blank=True, null=True)
    all_fatalities = models.FloatField(blank=True, null=True)
    property_damage_costs = models.FloatField(blank=True, null=True)
    lost_commodity_costs = models.FloatField(blank=True, null=True)
    public_private_property_damage_costs = models.FloatField(db_column='public/private_property_damage_costs', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_response_costs = models.FloatField(blank=True, null=True)
    environmental_remediation_costs = models.FloatField(blank=True, null=True)
    other_costs = models.FloatField(blank=True, null=True)
    all_costs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'database'


class DpLive02012022050459635(models.Model):
    location = models.TextField(blank=True, null=True)
    indicator = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    measure = models.TextField(blank=True, null=True)
    frequency = models.TextField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    flag_codes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dp_live_02012022050459635'


class GlobalCrudePetroleumTrade19952021(models.Model):
    continent = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    trade_value = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_crude_petroleum_trade_1995_2021'


class OilAndGas(models.Model):
    symbol = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oil_and_gas'


class OilAndGas19322014(models.Model):
    cty_name = models.TextField(blank=True, null=True)
    iso3numeric = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=50, primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    eiacty = models.TextField(blank=True, null=True)
    oil_prod32_14 = models.FloatField(blank=True, null=True)
    oil_price_2000 = models.FloatField(blank=True, null=True)
    oil_price_nom = models.FloatField(blank=True, null=True)
    oil_value_nom = models.FloatField(blank=True, null=True)
    oil_value_2000 = models.FloatField(blank=True, null=True)
    oil_value_2014 = models.FloatField(blank=True, null=True)
    gas_prod55_14 = models.FloatField(blank=True, null=True)
    gas_price_2000_mboe = models.FloatField(blank=True, null=True)
    gas_price_2000 = models.FloatField(blank=True, null=True)
    gas_price_nom = models.FloatField(blank=True, null=True)
    gas_value_nom = models.FloatField(blank=True, null=True)
    gas_value_2000 = models.FloatField(blank=True, null=True)
    gas_value_2014 = models.FloatField(blank=True, null=True)
    oil_gas_value_nom = models.FloatField(blank=True, null=True)
    oil_gas_value_2000 = models.FloatField(blank=True, null=True)
    oil_gas_value_2014 = models.FloatField(blank=True, null=True)
    oil_gas_valuepop_nom = models.FloatField(blank=True, null=True)
    oil_gas_valuepop_2000 = models.FloatField(blank=True, null=True)
    oil_gas_valuepop_2014 = models.FloatField(blank=True, null=True)
    oil_exports = models.FloatField(blank=True, null=True)
    net_oil_exports = models.FloatField(blank=True, null=True)
    net_oil_exports_mt = models.FloatField(blank=True, null=True)
    net_oil_exports_value = models.FloatField(blank=True, null=True)
    net_oil_exports_valuepop = models.FloatField(blank=True, null=True)
    gas_exports = models.FloatField(blank=True, null=True)
    net_gas_exports_bcf = models.FloatField(blank=True, null=True)
    net_gas_exports_mboe = models.FloatField(blank=True, null=True)
    net_gas_exports_value = models.FloatField(blank=True, null=True)
    net_gas_exports_valuepop = models.FloatField(blank=True, null=True)
    net_oil_gas_exports_valuepop = models.FloatField(blank=True, null=True)
    population = models.FloatField(blank=True, null=True)
    pop_maddison = models.FloatField(blank=True, null=True)
    sovereign = models.IntegerField(blank=True, null=True)
    mult_nom_2000 = models.FloatField(blank=True, null=True)
    mult_nom_2014 = models.FloatField(blank=True, null=True)
    mult_2000_2014 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oil_and_gas_1932_2014'


class OilConsumptionByCountry1965To2023(models.Model):
    entity = models.TextField(blank=True, null=True)
    number_1965 = models.FloatField(db_column='1965', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1966 = models.FloatField(db_column='1966', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1967 = models.FloatField(db_column='1967', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1968 = models.FloatField(db_column='1968', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1969 = models.FloatField(db_column='1969', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1970 = models.FloatField(db_column='1970', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1971 = models.FloatField(db_column='1971', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1972 = models.FloatField(db_column='1972', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1973 = models.FloatField(db_column='1973', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1974 = models.FloatField(db_column='1974', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1975 = models.FloatField(db_column='1975', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1976 = models.FloatField(db_column='1976', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1977 = models.FloatField(db_column='1977', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1978 = models.FloatField(db_column='1978', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1979 = models.FloatField(db_column='1979', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1980 = models.FloatField(db_column='1980', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1981 = models.FloatField(db_column='1981', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1982 = models.FloatField(db_column='1982', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1983 = models.FloatField(db_column='1983', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1984 = models.FloatField(db_column='1984', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1985 = models.FloatField(db_column='1985', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1986 = models.FloatField(db_column='1986', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1987 = models.FloatField(db_column='1987', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1988 = models.FloatField(db_column='1988', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1989 = models.FloatField(db_column='1989', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1990 = models.FloatField(db_column='1990', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1991 = models.FloatField(db_column='1991', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1992 = models.FloatField(db_column='1992', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1993 = models.FloatField(db_column='1993', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1994 = models.FloatField(db_column='1994', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1995 = models.FloatField(db_column='1995', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1996 = models.FloatField(db_column='1996', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1997 = models.FloatField(db_column='1997', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1998 = models.FloatField(db_column='1998', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1999 = models.FloatField(db_column='1999', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2000 = models.FloatField(db_column='2000', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2001 = models.FloatField(db_column='2001', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2002 = models.FloatField(db_column='2002', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2003 = models.FloatField(db_column='2003', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2004 = models.FloatField(db_column='2004', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2005 = models.FloatField(db_column='2005', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2006 = models.FloatField(db_column='2006', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2007 = models.FloatField(db_column='2007', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2008 = models.FloatField(db_column='2008', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2009 = models.FloatField(db_column='2009', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2010 = models.FloatField(db_column='2010', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2011 = models.FloatField(db_column='2011', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2012 = models.FloatField(db_column='2012', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2013 = models.FloatField(db_column='2013', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2014 = models.FloatField(db_column='2014', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2015 = models.FloatField(db_column='2015', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2016 = models.FloatField(db_column='2016', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2017 = models.FloatField(db_column='2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2018 = models.FloatField(db_column='2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2019 = models.FloatField(db_column='2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2020 = models.FloatField(db_column='2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2021 = models.FloatField(db_column='2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2022 = models.FloatField(db_column='2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2023 = models.FloatField(db_column='2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'oil_consumption_by_country_1965_to_2023'


class OilProductionStatistics(models.Model):
    country_name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    product = models.TextField(blank=True, null=True)
    flow = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oil_production_statistics'


class OilSpill(models.Model):
    f_1 = models.IntegerField(blank=True, null=True)
    f_2 = models.IntegerField(blank=True, null=True)
    f_3 = models.FloatField(blank=True, null=True)
    f_4 = models.FloatField(blank=True, null=True)
    f_5 = models.IntegerField(blank=True, null=True)
    f_6 = models.IntegerField(blank=True, null=True)
    f_7 = models.FloatField(blank=True, null=True)
    f_8 = models.FloatField(blank=True, null=True)
    f_9 = models.FloatField(blank=True, null=True)
    f_10 = models.FloatField(blank=True, null=True)
    f_11 = models.FloatField(blank=True, null=True)
    f_12 = models.FloatField(blank=True, null=True)
    f_13 = models.FloatField(blank=True, null=True)
    f_14 = models.FloatField(blank=True, null=True)
    f_15 = models.FloatField(blank=True, null=True)
    f_16 = models.FloatField(blank=True, null=True)
    f_17 = models.FloatField(blank=True, null=True)
    f_18 = models.FloatField(blank=True, null=True)
    f_19 = models.FloatField(blank=True, null=True)
    f_20 = models.FloatField(blank=True, null=True)
    f_21 = models.FloatField(blank=True, null=True)
    f_22 = models.FloatField(blank=True, null=True)
    f_23 = models.IntegerField(blank=True, null=True)
    f_24 = models.FloatField(blank=True, null=True)
    f_25 = models.FloatField(blank=True, null=True)
    f_26 = models.FloatField(blank=True, null=True)
    f_27 = models.FloatField(blank=True, null=True)
    f_28 = models.FloatField(blank=True, null=True)
    f_29 = models.FloatField(blank=True, null=True)
    f_30 = models.FloatField(blank=True, null=True)
    f_31 = models.FloatField(blank=True, null=True)
    f_32 = models.FloatField(blank=True, null=True)
    f_33 = models.FloatField(blank=True, null=True)
    f_34 = models.FloatField(blank=True, null=True)
    f_35 = models.IntegerField(blank=True, null=True)
    f_36 = models.IntegerField(blank=True, null=True)
    f_37 = models.FloatField(blank=True, null=True)
    f_38 = models.FloatField(blank=True, null=True)
    f_39 = models.IntegerField(blank=True, null=True)
    f_40 = models.IntegerField(blank=True, null=True)
    f_41 = models.FloatField(blank=True, null=True)
    f_42 = models.FloatField(blank=True, null=True)
    f_43 = models.FloatField(blank=True, null=True)
    f_44 = models.FloatField(blank=True, null=True)
    f_45 = models.FloatField(blank=True, null=True)
    f_46 = models.IntegerField(blank=True, null=True)
    f_47 = models.FloatField(blank=True, null=True)
    f_48 = models.FloatField(blank=True, null=True)
    f_49 = models.FloatField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oil_spill'


class OilSpillageDataset(models.Model):
    spill_vessel = models.TextField(db_column='spill_/_vessel', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location = models.TextField(blank=True, null=True)
    dates = models.TextField(blank=True, null=True)
    min_tonnes = models.TextField(blank=True, null=True)
    max_tonnes = models.TextField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oil_spillage_dataset'


class PipelineMilesPerState(models.Model):
    state_code = models.CharField(primary_key=True, max_length=2)
    state_name = models.CharField(max_length=50)
    pipeline_miles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pipeline_miles_per_state'


class Spills1NumberOilSpills(models.Model):
    entity = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    large_oil_spills_700_tonnes_field = models.IntegerField(db_column='large_oil_spills_(>700_tonnes)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    medium_oil_spills_7_700_tonnes_field = models.IntegerField(db_column='medium_oil_spills_(7_700_tonnes)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'spills1_number_oil_spills'


class Spills2QuantityOilSpills(models.Model):
    entity = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    quantity_of_oil_spilled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spills2_quantity_oil_spills'


class Spills3LargeOilSpillsDecadal(models.Model):
    entity = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    decadal_large_oil_spills_700_tonnes_field = models.IntegerField(db_column='decadal_large_oil_spills_(>700_tonnes)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    decadal_medium_oil_spills_7_700_tonnes_field = models.IntegerField(db_column='decadal_medium_oil_spills_(7_700_tonnes)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'spills3_large_oil_spills_decadal'


class Spills4QuantityOilSpillsDecadalAverage(models.Model):
    entity = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    decadal_quantity_of_oil_spilled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spills4_quantity_oil_spills_decadal_average'


class Spills5NumberOfTankerSpillsByOperationAtTimeOfInciden(models.Model):
    entity = models.TextField(blank=True, null=True)
    code = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    at_anchor_inland_operations = models.FloatField(db_column='at_anchor_(inland)_operations', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bunkering_operations = models.FloatField(blank=True, null=True)
    other_operations = models.IntegerField(blank=True, null=True)
    underway_open_water_operations = models.FloatField(db_column='underway_(open_water)_operations', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    at_anchor_open_water_operations = models.FloatField(db_column='at_anchor_(open_water)_operations', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    loading_discharging_operations = models.IntegerField(db_column='loading/discharging_operations', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    underway_inland_operations = models.FloatField(db_column='underway_(inland)_operations', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    unknown_operations = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spills5_number_of_tanker_spills_by_operation_at_time_of_inciden'


class Spills6NumberOfTankerSpillsByPrimaryCauseOfSpill1970(models.Model):
    entity = models.TextField(blank=True, null=True)
    code = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    allision_collision_causes = models.IntegerField(db_column='allision/collision_causes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fire_explosion_causes = models.IntegerField(db_column='fire/explosion_causes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hull_failure_causes = models.IntegerField(blank=True, null=True)
    unknown_causes = models.IntegerField(blank=True, null=True)
    equipment_failure_causes = models.IntegerField(blank=True, null=True)
    grounding_causes = models.IntegerField(blank=True, null=True)
    other_causes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spills6_number_of_tanker_spills_by_primary_cause_of_spill_1970_'


class WorldCrudeOilReservesFrom1995To2021(models.Model):
    world_crude_oil_reserves_billion_field = models.TextField(db_column='world_crude_oil_reserves_(billion)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1995 = models.TextField(db_column='1995', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1996 = models.TextField(db_column='1996', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1997 = models.TextField(db_column='1997', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1998 = models.TextField(db_column='1998', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1999 = models.TextField(db_column='1999', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2000 = models.TextField(db_column='2000', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2001 = models.TextField(db_column='2001', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2002 = models.TextField(db_column='2002', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2003 = models.TextField(db_column='2003', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2004 = models.TextField(db_column='2004', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2005 = models.TextField(db_column='2005', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2006 = models.TextField(db_column='2006', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2007 = models.TextField(db_column='2007', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2008 = models.TextField(db_column='2008', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2009 = models.TextField(db_column='2009', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2010 = models.TextField(db_column='2010', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2011 = models.TextField(db_column='2011', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2012 = models.TextField(db_column='2012', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2013 = models.TextField(db_column='2013', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2014 = models.TextField(db_column='2014', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2015 = models.TextField(db_column='2015', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2016 = models.TextField(db_column='2016', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2017 = models.TextField(db_column='2017', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2018 = models.TextField(db_column='2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2019 = models.TextField(db_column='2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2020 = models.TextField(db_column='2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2021 = models.FloatField(db_column='2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'world_crude_oil_reserves_from_1995_to_2021'
