
import csv
import datetime

USERS = ['PATRICIA','GEORGIA','MATHEUS','GABRIELLE','RENATO','SHEILA']

def duracao(reg_entrada,reg_saida):
	if reg_saida != '':
		entrada = datetime.datetime.strptime(reg_entrada, '%H:%M:%S')
		saida = datetime.datetime.strptime(reg_saida, '%H:%M:%S')
		result = saida-entrada
		if (saida-entrada) > datetime.timedelta(hours=12):
			return 'Erro'
		else:
			return str(saida-entrada)	
	else:
		return 'Erro'

'''Criar registro do tipo data;hora_entrada;hora_saida;tempo_total'''
def create_csv(name, registros, datas):
	with open(name+'.csv', 'a', newline='\n', encoding='utf-8') as file:
		for data in datas:
			#pega todos os horarios da data
			iotimebydate = []
			for registro in registros:
				if registro[0] == data:
					iotimebydate.append(registro[1])

			'''caso os registros de hora do dia sejam impar deixo par'''
			if len(iotimebydate) % 2 == 1:
				iotimebydate.append('')

			'''Separa em duplas por data inicio-fim'''	
			reg_day=[]
			count=0
			for io in iotimebydate:
				if count < 2:
					reg_day.append(io)
					count+=1
				if count == 2:
					file.write( data + ";" + reg_day[0]+";"+reg_day[1]+";"+duracao(reg_day[0],reg_day[1]))
					file.write('\n')
					reg_day=[]
					print(reg_day)
					count = 0


		print("Arquivo '%s.csv' criado!"%name)

def read_csv(name):
	with open(name+'.csv', 'r', newline='\n', encoding='utf-8') as file:
		csvfile = csv.reader(file, delimiter=';')
		return csvfile

with open('ponto-teste.csv', 'r', newline='\n', encoding='utf-8') as file:
	csvfile = csv.reader(file, delimiter=';')
	linhas=[]
	for line in csvfile:
		linhas.append(line)

	for user in USERS:
		user_lines = []
		datas =[]
		for line in linhas:
			if line[4] == user:
				print(line)
				if line[0] not in datas:
					datas.append(line[0])
				user_lines.append(line)
		create_csv(user,user_lines,datas)
