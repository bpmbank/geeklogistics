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
        var map = new BMap.Map("j-map");//在百度地图容器中创建一个地图
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
    var markerArr = [{title:"极客总部-北京极客罗杰斯特有限公司",content:"电话：400-106-1234<br/>地址：北京百富达物流有限责任公司，成立于2010年5月，总部位于北京市大兴区黄村镇芦求路周村中街东路临11号",point:"116.30533|39.714144",isOpen:0,icon:{w:21,h:21,l:46,t:46,x:1,lb:10}}
		 ,{title:"极客-大兴站",content:"电话：400-106-1234<br/>地址：北京市朝阳区朝阳广渠东路33号沿海赛洛城314号楼底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.511883|39.903303",isOpen:0,icon:{w:23,h:25,l:43,t:21,x:6,lb:12}}
		 ,{title:"极客-望京站",content:"电话：400-106-1234<br/>地址：北京市昌平区回龙观天露园2区104号底商<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.322722|40.086445",isOpen:0,icon:{w:23,h:25,l:43,t:21,x:9,lb:12}}
		 ,{title:"极客-知春路",content:"电话：400-106-1234<br/>地址：北京市丰台区光彩路68号院东区2号楼1层<br/><br/>详细：黑狗冷链宅配是为了保障对于配送温度控制方面要求较高的生鲜类、冻品类商品品质，通过特殊工具及设备进行同城的全程冷运配送，针对电商客户所推出的专属服务。",point:"116.422621|39.84444",isOpen:0,icon:{w:23,h:25,l:43,t:21,x:9,lb:12}}
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
        var icon = new BMap.Icon("http://morry.oss-cn-beijing.aliyuncs.com/geek/us_mk_icon.png", new BMap.Size(json.w,json.h),{imageOffset: new BMap.Size(-json.l,-json.t),infoWindowOffset:new BMap.Size(json.lb+5,1),offset:new BMap.Size(json.x,json.h)})
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