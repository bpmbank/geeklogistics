    //创建和初始化地图函数：
    function initMap(){
        createMap();//创建地图
        setMapEvent();//设置地图事件
        addMapControl();//向地图添加控件
        addMarker();//向地图中添加marker
        addRemark();//向地图中添加文字标注
    }
    
    //创建地图函数：
    function createMap(){
        var map = new BMap.Map("dituContent");//在百度地图容器中创建一个地图
        var point = new BMap.Point(116.442788,39.918034);//定义一个中心点坐标
        map.centerAndZoom(point,11);//设定地图的中心点和坐标并将地图显示在地图容器中
        window.map = map;//将map变量存储在全局
    }
    
    //地图事件设置函数：
    function setMapEvent(){
        map.enableDragging();//启用地图拖拽事件，默认启用(可不写)
        map.enableScrollWheelZoom();//启用地图滚轮放大缩小
        map.enableDoubleClickZoom();//启用鼠标双击放大，默认启用(可不写)
        map.enableKeyboard();//启用键盘上下左右键移动地图
    }
    
    //地图控件添加函数：
    function addMapControl(){
        //向地图中添加缩放控件
	var ctrl_nav = new BMap.NavigationControl({anchor:BMAP_ANCHOR_TOP_RIGHT,type:BMAP_NAVIGATION_CONTROL_ZOOM});
	map.addControl(ctrl_nav);
        //向地图中添加缩略图控件
	var ctrl_ove = new BMap.OverviewMapControl({anchor:BMAP_ANCHOR_BOTTOM_RIGHT,isOpen:0});
	map.addControl(ctrl_ove);
        //向地图中添加比例尺控件
	var ctrl_sca = new BMap.ScaleControl({anchor:BMAP_ANCHOR_BOTTOM_RIGHT});
	map.addControl(ctrl_sca);
    }
    
    //标注点数组
    var markerArr = [{title:"黑狗总部-北京百富达物流有限责任公司",content:"电话：400-106-1234<br/>地址：北京百富达物流有限责任公司，成立于2010年5月，总部位于北京市大兴区黄村镇芦求路周村中街东路临11号",point:"116.30533|39.714144",isOpen:0,icon:{w:21,h:21,l:46,t:46,x:1,lb:10}}
		 ,{title:"黑狗-百子湾分部",content:"电话：400-106-1234<br/>地址：北京市朝阳区朝阳广渠东路33号沿海赛洛城314号楼底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.511883|39.903303",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-白家楼分部",content:"电话：400-106-1234<br/>地址：北京市朝阳区高碑店乡白家楼9号<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。电话：400-106-1234<br/>地址：<br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.553688|39.933829",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-回龙观分部",content:"电话：400-106-1234<br/>地址：北京市昌平区回龙观天露园2区104号底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.322722|40.086445",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-京深分部",content:"电话：400-106-1234<br/>地址：北京市丰台区光彩路68号院东区2号楼1层<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.422621|39.84444",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-立水桥分部",content:"电话：400-106-1234<br/>地址：北京市朝阳区立清路明天第一城7号院7号楼1层底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.419918|40.05253",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-石景山分部",content:"电话：400-106-1234<br/>地址：北京市石景山区杨庄大街85-1号平房<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.185528|39.920308",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-顺义分部",content:"电话：400-106-1234<br/>地址：北京市顺义区顺于路华英园小区5号楼5号底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.626451|40.135453",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-四道口分部",content:"电话：400-106-1234<br/>地址：北京市海淀区四道口大钟寺13号院内16号<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.346275|39.969871",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-通州分部",content:"电话：400-106-1234<br/>地址：北京市通州区永顺南街143号馨通家园底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.651042|39.921199",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-万泉河分部",content:"电话：400-106-1234<br/>地址：北京市海淀区万泉河路甲54号<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.307582|39.99258",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-马连洼分部",content:"电话：400-106-1234<br/>地址：北京市海淀区马连洼北路128号武警印刷厂房屋一层<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.293106|40.04093",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-亮马桥分部",content:"电话：400-106-1234<br/>地址：北京市朝阳区亮马桥路27号国际珠宝古玩城内停车场院内10号<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.480971|39.960207",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-望京分部",content:"电话：400-106-1234<br/>地址：北京市朝阳区利泽西街8号院东湖湾2号楼底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.469647|40.013395",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-武圣路分部",content:"电话：400-106-1234<br/>地址：北京市朝阳区武圣路松榆东里社区北一门<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.479089|39.877906",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-西南郊分部",content:"电话：400-106-1234<br/>地址：北京市丰台区南三环西路85号西南郊批发市场内11-12号<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.346751|39.855463",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-岳各庄分部",content:"电话：400-106-1234<br/>地址：北京市丰台区西四环中路碾子坟村<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.27945|39.883519",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-菜市口分部",content:"电话：400-106-1234<br/>地址：北京市宣武区岳峰园三区1号<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.379035|39.896653",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-新发地分部",content:"电话：400-106-1234<br/>地址：北京市丰台区银地家园8号楼底商8-4号<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.338416|39.824888",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ,{title:"黑狗-亦庄分部",content:"电话：400-106-1234<br/>地址：北京市亦庄经济开发区境界家园51号楼底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.492633|39.802532",isOpen:0,icon:{w:23,h:25,l:46,t:21,x:9,lb:12}}
		 ];
    //创建marker
    function addMarker(){
        for(var i=0;i<markerArr.length;i++){
            var json = markerArr[i];
            var p0 = json.point.split("|")[0];
            var p1 = json.point.split("|")[1];
            var point = new BMap.Point(p0,p1);
			var iconImg = createIcon(json.icon);
            var marker = new BMap.Marker(point,{icon:iconImg});
			var iw = createInfoWindow(i);
			var label = new BMap.Label(json.title,{"offset":new BMap.Size(json.icon.lb-json.icon.x+10,-20)});
			marker.setLabel(label);
            map.addOverlay(marker);
            label.setStyle({
                        borderColor:"#808080",
                        color:"#333",
                        cursor:"pointer"
            });
			
			(function(){
				var index = i;
				var _iw = createInfoWindow(i);
				var _marker = marker;
				_marker.addEventListener("click",function(){
				    this.openInfoWindow(_iw);
			    });
			    _iw.addEventListener("open",function(){
				    _marker.getLabel().hide();
			    })
			    _iw.addEventListener("close",function(){
				    _marker.getLabel().show();
			    })
				label.addEventListener("click",function(){
				    _marker.openInfoWindow(_iw);
			    })
				if(!!json.isOpen){
					label.hide();
					_marker.openInfoWindow(_iw);
				}
			})()
        }
    }
    //创建InfoWindow
    function createInfoWindow(i){
        var json = markerArr[i];
        var iw = new BMap.InfoWindow("<b class='iw_poi_title' title='" + json.title + "'>" + json.title + "</b><div class='iw_poi_content'>"+json.content+"</div>");
        return iw;
    }
    //创建一个Icon
    function createIcon(json){
        var icon = new BMap.Icon("http://www.bfd-logistics.com/index/Tpl/default/www/us_mk_icon.png", new BMap.Size(json.w,json.h),{imageOffset: new BMap.Size(-json.l,-json.t),infoWindowOffset:new BMap.Size(json.lb+5,1),offset:new BMap.Size(json.x,json.h)})
        return icon;
    }
//文字标注数组
    var lbPoints = [{point:"116.624068|40.157348",content:""}
		 ];
    //向地图中添加文字标注函数
    function addRemark(){
        for(var i=0;i<lbPoints.length;i++){
            var json = lbPoints[i];
            var p1 = json.point.split("|")[0];
            var p2 = json.point.split("|")[1];
            var label = new BMap.Label("<div style='padding:2px;'>"+json.content+"</div>",{point:new BMap.Point(p1,p2),offset:new BMap.Size(3,-6)});
            map.addOverlay(label);
            label.setStyle({borderColor:"#999"});
        }
    }
    
    initMap();//创建和初始化地图