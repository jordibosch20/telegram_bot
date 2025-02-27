grammar Sky;
root : skyline EOF;
skyline :  VAR ASSIG (crear | operacio) | operacio;

crear: simple|compost|aleatori;

operacio: '(' operacio ')'| '-' (VAR|crear|operacio) | operacio ('*'|'+'|'-') (NUM|operacio) | (crear|VAR);	


simple : edifici;
compost : OC edifici (COMA edifici)* TC;
aleatori : OB edaleatori CB;

edifici : PO NUM COMA NUM COMA NUM PT;
edaleatori : NUM COMA NUM COMA NUM COMA NUM COMA NUM;

MES : '+';
MENYS : '-';
MULT : '*';

VAR : ('a'..'z' | 'A'..'Z') ('a'..'z' | 'A'..'Z' | NUM)* ;

OC : '[';
TC : ']';

OB : '{';
CB : '}';

ASSIG : ':=' ;
PO : '(';
PT : ')';
COMA : ',';
NUM : [0-9]+ ;
WS : [ \n]+ -> skip ;