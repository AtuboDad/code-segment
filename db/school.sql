	-- public.edu_school definition

-- Drop table

DROP TABLE public.edu_school;

CREATE TABLE public.edu_school (
	id int8 NOT NULL DEFAULT nextval('public.edu_school_id_seq'::regclass),
	type varchar(32) NULL, -- 类型
	organization_name varchar(255) NULL, -- 机构名称
	organization_code varchar(255) NULL, -- 机构编码
	operation_type varchar(255) NULL, -- 办学类型
	operation_type_code varchar(255) NULL, -- 办学类型编码
	sponsor_nature varchar(255) NULL, -- 举办者性质
	sponsor_type_group varchar(255) NULL, -- 举办者类型分组
	sponsor_type varchar(255) NULL, -- 举办者类型
	sponsor_type_code varchar(255) NULL, -- 举办者类型编码
	urban_group varchar(255) NULL, -- 城乡分组
	urban_type varchar(255) NULL, -- 城乡类型
	urban_type_code varchar(255) NULL, -- 城乡类型编码
	university_type varchar(255) NULL, -- 高校类型
	is_counted int2 NULL, -- 是否计校数
	is_withdrawn_last_year int2 NULL, -- 是否上年撤销
	is_new_this_year int2 NULL, -- 是否本年新增
	is_national int2 NULL, -- 是否民族
	has_bilingual_class int2 NULL, -- 是否具有双语教学班
	is_inclusive_privacy int2 NULL, -- 是否普惠性民办幼儿园
	credit_code varchar(255) NULL, -- 法人和其他组织统一社会信用代码
	is_town_center_kindergarten int2 NULL, -- 是否乡镇中心幼儿园
	is_town_center_school int2 NULL, -- 是否乡镇中心小学
	has_attached_class int2 NULL, -- 是否具有附设班
	is_affiliated_school int2 NULL, -- 是否附属学校(园)
	affiliated_college_name varchar(255) NULL, -- 附属于高校机构名称
	is_profitable int2 NULL, -- 是否营利性
	profitable_abbreviation varchar(255) NULL, -- 营利性民办学校(机构)简称
	location_code varchar(255) NULL, -- 所在地区编码
	location_level_one varchar(255) NULL, -- 所在地区划一级
	location_level_two varchar(255) NULL, -- 所在地区划二级
	location_level_three varchar(255) NULL, -- 所在地区划三级
	location_level_four varchar(255) NULL, -- 所在地区划四级
	location_level_five varchar(255) NULL, -- 所在地区划五级
	statistical_agency_code varchar(255) NULL, -- 统计机构编码
	statistical_level_one varchar(255) NULL, -- 统计一级
	statistical_level_two varchar(255) NULL, -- 统计二级
	statistical_level_three varchar(255) NULL, -- 统计三级
	collection_agency_code varchar(255) NULL, -- 采集机构编码
	collection_level_one varchar(255) NULL, -- 采集一级
	collection_level_two varchar(255) NULL, -- 采集二级
	collection_level_three varchar(255) NULL, -- 采集三级
	collection_level_four varchar(255) NULL, -- 采集四级
	collection_level_five varchar(255) NULL, -- 采集五级
	longitude numeric NULL, -- 经度
	latitude numeric NULL, -- 纬度
	indicator_name varchar(255) NULL, -- 指标名称
	headmaster varchar(32) NULL, -- 校长姓名
	statistical_officer varchar(32) NULL, -- 统计负责人
	statistical_officer_dept varchar(32) NULL, -- 统计负责人部门
	statistical_officer_post varchar(128) NULL, -- 统计负责人职务
	fill_user varchar(32) NULL, -- 填表人
	fill_user_dept varchar(32) NULL, -- 填表人部门
	fill_user_post varchar(128) NULL, -- 填表人职务
	fill_user_phone varchar(32) NULL, -- 填表人电话
	zip_code varchar(32) NULL, -- 邮编
	phone_area_no varchar(32) NULL, -- 电话区号
	office_phone varchar(32) NULL, -- 办公电话
	office_mobile varchar(32) NULL, -- 移动电话
	website varchar(256) NULL, -- 网址
	mail varchar(128) NULL, -- 邮箱地址
	electrify int4 NULL, -- 是否通电
	network_method varchar(32) NULL, -- 接入网络方式
	wireless_network varchar(32) NULL, -- 是否无线网全覆盖
	water_supply_method varchar(32) NULL, -- 供水方式
	toilet_situation varchar(64) NULL, -- 厕所情况
	washing varchar(64) NULL, -- 洗手设施
	build_parent_committee varchar(64) NULL, -- 建立家长委员会
	security_personnel_num int4 NULL, -- 安防人员人数
	create_time timestamp NULL, -- 创建时间
	create_by varchar(32) NULL, -- 创建人
	update_time timestamp NULL, -- 更新时间
	update_by varchar(32) NULL, -- 更新人
	status int4 NULL, -- 状态
	CONSTRAINT edu_school_pk PRIMARY KEY (id)
);
COMMENT ON TABLE public.edu_school IS '学校信息表';

-- Column comments

COMMENT ON COLUMN public.edu_school.id IS '主键ID';
COMMENT ON COLUMN public.edu_school.type IS '类型';
COMMENT ON COLUMN public.edu_school.organization_name IS '机构名称';
COMMENT ON COLUMN public.edu_school.organization_code IS '机构编码';
COMMENT ON COLUMN public.edu_school.operation_type IS '办学类型';
COMMENT ON COLUMN public.edu_school.operation_type_code IS '办学类型编码';
COMMENT ON COLUMN public.edu_school.sponsor_nature IS '举办者性质';
COMMENT ON COLUMN public.edu_school.sponsor_type_group IS '举办者类型分组';
COMMENT ON COLUMN public.edu_school.sponsor_type IS '举办者类型';
COMMENT ON COLUMN public.edu_school.sponsor_type_code IS '举办者类型编码';
COMMENT ON COLUMN public.edu_school.urban_group IS '城乡分组';
COMMENT ON COLUMN public.edu_school.urban_type IS '城乡类型';
COMMENT ON COLUMN public.edu_school.urban_type_code IS '城乡类型编码';
COMMENT ON COLUMN public.edu_school.university_type IS '高校类型';
COMMENT ON COLUMN public.edu_school.is_counted IS '是否计校数';
COMMENT ON COLUMN public.edu_school.is_withdrawn_last_year IS '是否上年撤销';
COMMENT ON COLUMN public.edu_school.is_new_this_year IS '是否本年新增';
COMMENT ON COLUMN public.edu_school.is_national IS '是否民族';
COMMENT ON COLUMN public.edu_school.has_bilingual_class IS '是否具有双语教学班';
COMMENT ON COLUMN public.edu_school.is_inclusive_privacy IS '是否普惠性民办幼儿园';
COMMENT ON COLUMN public.edu_school.credit_code IS '法人和其他组织统一社会信用代码';
COMMENT ON COLUMN public.edu_school.is_town_center_kindergarten IS '是否乡镇中心幼儿园';
COMMENT ON COLUMN public.edu_school.is_town_center_school IS '是否乡镇中心小学';
COMMENT ON COLUMN public.edu_school.has_attached_class IS '是否具有附设班';
COMMENT ON COLUMN public.edu_school.is_affiliated_school IS '是否附属学校(园)';
COMMENT ON COLUMN public.edu_school.affiliated_college_name IS '附属于高校机构名称';
COMMENT ON COLUMN public.edu_school.is_profitable IS '是否营利性';
COMMENT ON COLUMN public.edu_school.profitable_abbreviation IS '营利性民办学校(机构)简称';
COMMENT ON COLUMN public.edu_school.location_code IS '所在地区编码';
COMMENT ON COLUMN public.edu_school.location_level_one IS '所在地区划一级';
COMMENT ON COLUMN public.edu_school.location_level_two IS '所在地区划二级';
COMMENT ON COLUMN public.edu_school.location_level_three IS '所在地区划三级';
COMMENT ON COLUMN public.edu_school.location_level_four IS '所在地区划四级';
COMMENT ON COLUMN public.edu_school.location_level_five IS '所在地区划五级';
COMMENT ON COLUMN public.edu_school.statistical_agency_code IS '统计机构编码';
COMMENT ON COLUMN public.edu_school.statistical_level_one IS '统计一级';
COMMENT ON COLUMN public.edu_school.statistical_level_two IS '统计二级';
COMMENT ON COLUMN public.edu_school.statistical_level_three IS '统计三级';
COMMENT ON COLUMN public.edu_school.collection_agency_code IS '采集机构编码';
COMMENT ON COLUMN public.edu_school.collection_level_one IS '采集一级';
COMMENT ON COLUMN public.edu_school.collection_level_two IS '采集二级';
COMMENT ON COLUMN public.edu_school.collection_level_three IS '采集三级';
COMMENT ON COLUMN public.edu_school.collection_level_four IS '采集四级';
COMMENT ON COLUMN public.edu_school.collection_level_five IS '采集五级';
COMMENT ON COLUMN public.edu_school.longitude IS '经度';
COMMENT ON COLUMN public.edu_school.latitude IS '纬度';
COMMENT ON COLUMN public.edu_school.indicator_name IS '指标名称';
COMMENT ON COLUMN public.edu_school.headmaster IS '校长姓名';
COMMENT ON COLUMN public.edu_school.statistical_officer IS '统计负责人';
COMMENT ON COLUMN public.edu_school.statistical_officer_dept IS '统计负责人部门';
COMMENT ON COLUMN public.edu_school.statistical_officer_post IS '统计负责人职务';
COMMENT ON COLUMN public.edu_school.fill_user IS '填表人';
COMMENT ON COLUMN public.edu_school.fill_user_dept IS '填表人部门';
COMMENT ON COLUMN public.edu_school.fill_user_post IS '填表人职务';
COMMENT ON COLUMN public.edu_school.fill_user_phone IS '填表人电话';
COMMENT ON COLUMN public.edu_school.zip_code IS '邮编';
COMMENT ON COLUMN public.edu_school.phone_area_no IS '电话区号';
COMMENT ON COLUMN public.edu_school.office_phone IS '办公电话';
COMMENT ON COLUMN public.edu_school.office_mobile IS '移动电话';
COMMENT ON COLUMN public.edu_school.website IS '网址';
COMMENT ON COLUMN public.edu_school.mail IS '邮箱地址';
COMMENT ON COLUMN public.edu_school.electrify IS '是否通电';
COMMENT ON COLUMN public.edu_school.network_method IS '接入网络方式';
COMMENT ON COLUMN public.edu_school.wireless_network IS '是否无线网全覆盖';
COMMENT ON COLUMN public.edu_school.toilet_situation IS '学校厕所情况';
COMMENT ON COLUMN public.edu_school.washing IS '洗手设施';
COMMENT ON COLUMN public.edu_school.build_parent_committee IS '建立家长委员会';
COMMENT ON COLUMN public.edu_school.water_supply_method IS '供水方式';
COMMENT ON COLUMN public.edu_school.security_personnel_num IS '安防人员人数';
COMMENT ON COLUMN public.edu_school.create_time IS '创建时间';
COMMENT ON COLUMN public.edu_school.create_by IS '创建人';
COMMENT ON COLUMN public.edu_school.update_time IS '更新时间';
COMMENT ON COLUMN public.edu_school.update_by IS '更新人';
COMMENT ON COLUMN public.edu_school.status IS '状态';