# -*- coding: utf-8 -*-
import uuid
from sqlalchemy.sql import func
from stackshare.database import require_connection,Service,ServiceReason
from database import ensure_schema

ensure_schema()

class StacksharePipeline(object):
    def process_item(self, item, spider):
        if type(item).__name__=='StackTypeName':
            pass
        else:
            self.insert_db(item)
    

    @require_connection
    def insert_db(self,item,conn=None):
        service_id=str(uuid.uuid4())
        ins=Service.insert().values(service_id=service_id,service_name=item['name'],service_title=item['title'],service_image_url=item['img_url'],
                                  service_description=item['description'],service_type='saas',category_name='SAAS_SERVICE',created_at=func.now())
        conn.execute(ins)
        for reason in item['reason'].items():
            s=ServiceReason.insert().values(service_id=service_id,service_reason_name=reason[0],service_reason_count=reason[1],created_at=func.now())
            conn.execute(s)
            
            
            
                                                                                                                                                                                               
