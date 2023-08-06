from mindsdb.api.mysql.mysql_proxy.datahub.information_schema import InformationSchema
from mindsdb.api.mysql.mysql_proxy.datahub.datanodes.mindsdb_datanode import MindsDBDataNode
from mindsdb.api.mysql.mysql_proxy.datahub.datanodes.datasource_datanode import DataSourceDataNode
from mindsdb.api.mysql.mysql_proxy.datahub.datanodes.integration_datanode import IntegrationDataNode
from mindsdb.interfaces.database.integrations import DatasourceController


def init_datahub(model_interface, ai_table, data_store, company_id=None):
    datahub = InformationSchema()

    datahub.add({
        'mindsdb': MindsDBDataNode(model_interface, ai_table, data_store, company_id),
        'datasource': DataSourceDataNode(data_store)
    })

    integrations = DatasourceController().get_db_integrations(company_id).keys()
    for key in integrations:
        datahub.add({
            key: IntegrationDataNode(key, data_store)
        })

    return datahub
