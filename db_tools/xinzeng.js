//返回强制重新加载
window.onpageshow = function(event) {
	if(event.persisted) {
		window.location.reload();
	}
}
//定义数组
var arrayObj = new Array();
//新老用户状态
var state = 0;

$.ajax({
url: "appurl",
type: "POST",
dataType: "json",
success: function (data) {
	alert(data.status);
	console.log(data)}

})

//网络故障
$(function() {　
	$(document).ready(function() {
		if(navigator.onLine) {
			$("#no_network").hide();
			$(".container").show();
			if(state == 0) {
				$(".new_user").show();
				$(".old_user").hide();
			} else {
				$(".new_user").hide();
				$(".old_user").show();
			}
		} else {
			noNetwork();
			$(".container").hide();
		}
	});

	//	新增人员
	$(".add_img").click(function() {
		$(".xinzeng_mask").show();
	});

	//	新增人员选择关系
	$("#xiala").click(function() {
		$(".select_guanxi").show();
	});
	$(".select_block ul li").click(function() {
		$(this).addClass("select_active").siblings().removeClass("select_active");
		var guanxi = $(this).html();
		$("#xiala").val(guanxi);
		setTimeout(function() {
			$(".select_guanxi").hide();
		}, 500);
	});
	$(".select_close").click(function() {
		$(".select_guanxi").hide();
	});
	//	更换人员
	$("#showBank").click(function() {
		$(".change_guanxi").show();
	});

	//领取跳转页面
	$("#lingqu_btn").click(function() {
		//姓名
		var bzName = $.trim($(".old_user #old_user_name").html());
		sessionStorage.setItem("bzName", bzName);
		//		身份证号
		var idCard = $.trim($(".old_user #old_user_idcard").html());
		var Idcard = $.base64.encode(idCard);
		sessionStorage.setItem("Idcard", Idcard);
		//		手机号
		var Mobile = $.trim($(".old_user #old_user_phone").html());
		var Mobile = $.base64.encode(Mobile);
		sessionStorage.setItem("Mobile", Mobile);
		//		关系
		var relation = $.trim($(".old_user #old_user_relation").html());
		sessionStorage.setItem("relation", relation);
		//		跳转 
		var checked = $(".footer_xieyi").find("#check1").is(':checked') == true;
		if((bzName.length>0)&&(idCard.length>0)&&(Mobile.length>0)&&(relation.length>0)&&(checked == true)) {
			location.href = 'health.html';
		}
	});

	//	身份证号输入控制
	$(".shenfenz").on("input", function() {
		var arr = []
		var txt = /\d|X/
		for(let i = 0; i < $(this).val().length; i++) {
			if(Object.prototype.toString.call(($(this).val()[i]) - 0) === "[object Number]" && ($(this).val()[i] - 0) + '' !== 'NaN') {

			} else if($(this).val()[i] == "X" && i == 17) {

			} else if($(this).val()[i] == "x" && i == 17) {
				$(this).val($(this).val().toUpperCase());
			} else {
				$(this).focus();
				$(this).val($(this).val().replace(/[^\d]/g, ""));
			}
		}
	})
});

//验证手机号码
function checkPhone() {
	var phone = $("input[name='Tel']").val();
	phone = phone.replace(/\s/g, "");
	var pattern = /^[1][3,4,5,6,7,8,9][0-9]{9}$/;
	if(phone.length == 0) {
		return false;
	}
	if(!pattern.test(phone)) {
		return false;
	}
	return true;
}

//更换人员方法

var showBankDom = document.querySelector('#showBank');
//var bankIdDom = document.querySelector('#bankId');
var form_name = document.querySelector('#old_user_name');
var form_idcard = document.querySelector('#old_user_idcard');
var form_phone = document.querySelector('#old_user_phone');
var form_relation = document.querySelector('#old_user_relation');
//保存按钮
var saveXinzeng = document.querySelector('#save_btn');

//新增保存方法

saveXinzeng.addEventListener('click', function() {
	var name = $("#Name").val();
	var ID = $("#ID").val();
	var telphone = $("#mobile").val();
	var relation = $("#xiala").val();
	if((telphone.length == 11) && checkPhone() && ($("#ID").val().length == 18 || $("#ID").val().length == 15) && isIdCardNo() && ($("#Name").val().length > 1) && ($("#xiala").val().length > 0)) {
		$(".new_user").hide();
		$(".xinzeng_mask").hide();
		$(".old_user").show();
		console.log(state);
		//		将值保存在一个数组
		var newArr = {};
		var shuzuId = arrayObj.length + 1;
		newArr.id = shuzuId;
		newArr.name = $("#Name").val();
		newArr.idCard = $("#ID").val();
		newArr.phoneNumber = $("#mobile").val();
		newArr.relation = $("#xiala").val();
		arrayObj.push(newArr);
		console.log(arrayObj);
		if((state == 0) && (arrayObj.length == 1)) {
			$(".old_user #old_user_name").html("");
			$(".old_user #old_user_idcard").html("");
			$(".old_user #old_user_phone").html("");
			$(".old_user #old_user_relation").html("");
			$(".old_user #old_user_name").html(name);
			$(".old_user #old_user_idcard").html(ID);
			$(".old_user #old_user_phone").html(telphone);
			$(".old_user #old_user_relation").html(relation);
		} else if((state == 0) && (arrayObj.length > 1)) {
			var data = [].concat(arrayObj);
			var personSelect = new IosSelect(1, [data], {
				container: '.change_container_old',
				title: '选择人员',
				itemHeight: 50,
				itemShowCount: 5,
				oneLevelId: baocunId,
				callback: function(selectOneObj) {
					form_name.innerHTML = selectOneObj.name;
					console.log(selectOneObj);
					form_idcard.innerHTML = selectOneObj.idcard;
					form_phone.innerHTML = selectOneObj.phonenumber;
					form_relation.innerHTML = selectOneObj.relation;
				}
			});
		} else if(state == 1) {
			var data = [{
					"idCard": "110101199503070341",
					"name": "赵俊杰1",
					"phoneNumber": "15203118342",
					"state": 1,
					"user_id": "wangerxiao"
				},
				{
					"idCard": "110101199603074737",
					"name": "王二小2",
					"phoneNumber": "18867564532",
					"state": 1,
					"user_id": "wangerxiao"
				}
			];
			var data = data.concat(arrayObj);
			var personSelect = new IosSelect(1, [data], {
				container: '.change_container_old',
				title: '选择人员',
				itemHeight: 50,
				itemShowCount: 5,
				oneLevelId: baocunId,
				callback: function(selectOneObj) {
					form_name.innerHTML = selectOneObj.name;
					console.log(selectOneObj);
					form_idcard.innerHTML = selectOneObj.idcard;
					form_phone.innerHTML = selectOneObj.phonenumber;
					form_relation.innerHTML = selectOneObj.relation;
				}
			});
		} else {
			return false;
		}

	} else if($("#Name").val().length == 0) {
		$(".tips_msg").show();
		$(".tips_msg p").html("请填写被保人姓名");
		setTimeout(function() {
			$(".tips_msg").hide();
		}, 3000);
	} else if($("#ID").val().length == 0) {
		$(".tips_msg").show();
		$(".tips_msg p").html("请填写被保人身份证号");
		setTimeout(function() {
			$(".tips_msg").hide();
		}, 3000);
	} else if($("#mobile").val().length == 0) {
		$(".tips_msg").show();
		$(".tips_msg p").html("请填写被保人联系方式");
		setTimeout(function() {
			$(".tips_msg").hide();
		}, 3000);
	} else if($("#xiala").val().length == 0) {
		$(".tips_msg").show();
		$(".tips_msg p").html("请选择被保人与你的关系");
		setTimeout(function() {
			$(".tips_msg").hide();
		}, 3000);
	} else if(($("#ID").val().length > 0) && (!isIdCardNo())) {
		$(".tips_msg").show();
		$(".tips_msg p").html("请输入正确格式的身份证号");
		setTimeout(function() {
			$(".tips_msg").hide();
		}, 3000);
	} else if(($("#mobile").val().length > 0) && (!checkPhone())) {
		$(".tips_msg").show();
		$(".tips_msg p").html("请输入正确格式的手机号");
		setTimeout(function() {
			$(".tips_msg").hide();
		}, 3000);
	} else {
		$(".tips_msg").show();
		$(".tips_msg p").html("请核对输入信息是否正确");
		setTimeout(function() {
			$(".tips_msg").hide();
		}, 3000);
	}
});

//点击更换人员方法
showBankDom.addEventListener('click', function() {
	console.log(state);
	if(state == 0) {
		var data = [].concat(arrayObj);
	} else {
		var data = [{
				"idCard": "110101199503070341",
				"name": "赵俊杰1",
				"phoneNumber": "15203118342",
				"state": 1,
				"user_id": "wangerxiao"
			},
			{
				"idCard": "110101199603074737",
				"name": "王二小2",
				"phoneNumber": "18867564532",
				"state": 1,
				"user_id": "wangerxiao"
			}
		];
	}

	var bankSelect = new IosSelect(1, [data], {
		container: '.change_container',
		title: '选择人员',
		itemHeight: 50,
		itemShowCount: 5,
		oneLevelId: bankId,
		callback: function(selectOneObj) {
			//			bankIdDom.value = selectOneObj.id;
			//			bankIdDom.dataset['id'] = selectOneObj.id;
			//			bankIdDom.dataset['name'] = selectOneObj.name;
			console.log(selectOneObj);
			form_name.innerHTML = selectOneObj.name;
			form_idcard.innerHTML = selectOneObj.idcard;
			form_phone.innerHTML = selectOneObj.phonenumber;
			form_relation.innerHTML = selectOneObj.relation;
		}
	});
});

/**
 * 身份证校验算法
 */

function isIdCardNo() {
	var num = $("#ID").val();
	num = num.toUpperCase(); //身份证号码为15位或者18位，15位时全为数字，18位前17位为数字，最后一位是校验位，可能为数字或字符X。       
	if(!(/(^\d{15}$)|(^\d{17}([0-9]|X)$)/.test(num))) {
		//alert('输入的身份证号长度不对，或者号码不符合规定！\n15位号码应全为数字，18位号码末位可以为数字或X。');             
		//alert('身份证号长度不正确或不符合规定！');             
		return false;
	}
	//验证前2位，城市符合
	var aCity = {
		11: "北京",
		12: "天津",
		13: "河北",
		14: "山西",
		15: "内蒙古",
		21: "辽宁",
		22: "吉林",
		23: "黑龙江 ",
		31: "上海",
		32: "江苏",
		33: "浙江",
		34: "安徽",
		35: "福建",
		36: "江西",
		37: "山东",
		41: "河南",
		42: "湖北",
		43: "湖南",
		44: "广东",
		45: "广西",
		46: "海南",
		50: "重庆",
		51: "四川",
		52: "贵州",
		53: "云南",
		54: "西藏",
		61: "陕西",
		62: "甘肃",
		63: "青海",
		64: "宁夏",
		65: "新疆",
		71: "台湾",
		81: "香港",
		82: "澳门",
		91: "国外"
	};
	if(aCity[parseInt(num.substr(0, 2))] == null) {
		return false;
	}
	//下面分别分析出生日期和校验位
	var len, re;
	len = num.length;
	if(len == 15) {
		re = new RegExp(/^(\d{6})(\d{2})(\d{2})(\d{2})(\d{3})$/);
		var arrSplit = num.match(re); //检查生日日期是否正确
		var dtmBirth = new Date('19' + arrSplit[2] + '/' + arrSplit[3] + '/' + arrSplit[4]);
		var bGoodDay;
		bGoodDay = (dtmBirth.getYear() == Number(arrSplit[2])) && ((dtmBirth.getMonth() + 1) == Number(arrSplit[3])) && (dtmBirth.getDate() == Number(arrSplit[4]));
		if(!bGoodDay) {
			return false;
		} else { //将15位身份证转成18位 //校验位按照ISO 7064:1983.MOD 11-2的规定生成，X可以认为是数字10。       
			var arrInt = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2);
			var arrCh = new Array('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2');
			var nTemp = 0,
				i;
			num = num.substr(0, 6) + '19' + num.substr(6, num.length - 6);
			for(i = 0; i < 17; i++) {
				nTemp += num.substr(i, 1) * arrInt[i];
			}
			num += arrCh[nTemp % 11];
			return true;
		}
	}
	if(len == 18) {
		re = new RegExp(/^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$/);
		var arrSplit = num.match(re); //检查生日日期是否正确
		var dtmBirth = new Date(arrSplit[2] + "/" + arrSplit[3] + "/" + arrSplit[4]);
		var bGoodDay;
		bGoodDay = (dtmBirth.getFullYear() == Number(arrSplit[2])) && ((dtmBirth.getMonth() + 1) == Number(arrSplit[3])) && (dtmBirth.getDate() == Number(arrSplit[4]));
		if(!bGoodDay) {
			return false;
		} else { //检验18位身份证的校验码是否正确。 //校验位按照ISO 7064:1983.MOD 11-2的规定生成，X可以认为是数字10。
			var valnum;
			var arrInt = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2);
			var arrCh = new Array('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2');
			var nTemp = 0,
				i;
			for(i = 0; i < 17; i++) {
				nTemp += num.substr(i, 1) * arrInt[i];
			}
			valnum = arrCh[nTemp % 11];
			if(valnum != num.substr(17, 1)) {
				return false;
			}
			return true;
		}
	}
	return false;
};