$perline = 10

list_main = {
	'linguistics' => '一字多音審訂表',
	'edu_std1' => '常用標準字體表',
	'edu_std2' => '次常用標準字體表',
	'big5_lv1' => 'Big5常用',
	'big5_lv2' => 'Big5次常',
	'taigi_hakka' => '台客語漢字',
	'edu_dict' => '重編國語辭典',
	'fonts_ref' => '通用參考字表',
	'elementary' => '國小生字(參考)',
	'family' => '前600姓氏用字',
	'geographical' => '前1000地名用字'
}

list_feqA = {
	'feqA_00' => '前1000',
	'feqA_01' => '前2000',
	'feqA_02' => '前3000',
	'feqA_03' => '前4000',
	'feqA_04' => '前5000',
	'feqA_05' => '前6000',
	'feqA_06' => '前7000',
	'feqA_07' => '前8000',
	'feqA_08' => '前9000',
	'feqA_09' => '前10000',
	'feqA_vari' => '異體補充',
	'feqA_hk' => '粵語補充'
}

list_feqB = {
	'feqB_00' => '前1000',
	'feqB_01' => '前2000',
	'feqB_02' => '前3000',
	'feqB_03' => '前4000',
	'feqB_04' => '前5000',
	'feqB_05' => '前6000',
	'feqB_06' => '前7000',
	'feqB_07' => '前8000',
	'feqB_08' => '前9000',
	'feqB_09' => '前10000'
}

def add_table fx, fn, tag, tabs, not_last
	list = []
	f = File.open("#{fn}.txt", 'r:utf-8')
	f.each { |s|
		uni = s.split(/\t/)[0]
		list << (uni.to_i(16) <= 0xFFFF ? 'uni' : 'u') + uni
	}

	fx.puts "#{tabs}{"
	fx.puts "#{tabs}\tname = \"#{tag}\";"
	fx.puts "#{tabs}\tlist = ("
	list.each_with_index { |n, i|
		if i % $perline == 0
			fx.print "#{tabs}\t\t"
		end
		fx.print n
		fx.print ', ' if i < list.length-1

		fx.puts '' if (i+1) % $perline == 0
	}
	f.close
	fx.puts '' if list.length % $perline != 0
	fx.puts "#{tabs}\t);"
	fx.puts not_last ? "#{tabs}}," : "#{tabs}}"
end

def put_list fx, list, tabs, force_next
	cnt = 0
	list.each { |fn, tag|
		cnt += 1
		add_table(fx, fn, tag, tabs, force_next || cnt != list.size)
	}
end

fx = File.open('../ButTaiwanKit/Info/G3/Groups-Taiwan.plist', 'w:utf-8')
f = File.open('template.plist', 'r:utf-8')
#tabs = 0
f.each { |s|
	s.chomp!

	if s =~ /##ADD_HERE##/
		tabs = s.gsub(/[^\t]/, '')
		put_list fx, list_main, tabs, true

		fx.puts "#{tabs}{"
		fx.puts "#{tabs}\tname = \"網路字頻表\";"
		fx.puts "#{tabs}\tsubGroup = ("
		put_list fx, list_feqA, tabs+"\t\t", false
		fx.puts "#{tabs}\t);"
		fx.puts "#{tabs}},"

		fx.puts "#{tabs}{"
		fx.puts "#{tabs}\tname = \"字典字頻表\";"
		fx.puts "#{tabs}\tsubGroup = ("
		put_list fx, list_feqB, tabs+"\t\t", false
		fx.puts "#{tabs}\t);"
		fx.puts "#{tabs}}"
	else
		fx.puts s
	end
}
f.close
fx.close

f3 = File.open('../ButTaiwanKit/Info/G3/Groups-Taiwan.plist', 'r:utf-8')
f2 = File.open('../ButTaiwanKit/Info/G2/Groups.plist', 'w:utf-8')
f3.each { |s|
	f2.print s.gsub(/list\s*=\s*\(/, 'coverage = (')
}
f3.close
f2.close
