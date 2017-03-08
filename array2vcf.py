import sys
#first argument: the input tab file
header="##fileformat=VCFv4.1\n##source=ArrayVCFDB\n##ALT=<ID=DEL,Description=\"Deletion\">\n##ALT=<ID=DUP,Description=\"Duplication\">\n##INFO=<ID=SVTYPE,Number=1,Type=String,Description=\"Type of structural variant\">\n##INFO=<ID=END,Number=1,Type=String,Description=\"End of an intra-chromosomal variant\">\n##INFO=<ID=CLASS,Number=1,Type=String,Description=\"The classification(usually severity) of the variant\">\n##INFO=<ID=SVLEN,Number=1,Type=Integer,Description=\"Difference in length between REF and ALT alleles\">\n##FORMAT=<ID=GT,Number=1,Type=String,Description=\"Genotype\">"

print header

print "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tArrayDB"
id=0
for line in open(sys.argv[1]):
    if line[0] == "#":
       continue
    content=line.strip().split("\t")
    chrom = content[0]
    pos= content[1]
    end=content[2]
    var = "DUP"
    if content[3] == "Loss" or content[3] == "loss":
       var = "DEL"
    classification=content[-1]
    try:
       length=int(end)-int(pos)
    except:
       continue
    INFO="END={};SVTYPE={};SVLEN={};CLASS={}".format(end,var,length,classification)
    vcf_line=[chrom,pos,str(id),"N","<" +var + ">",".","PASS",INFO,"GT","./1"]
    print"\t".join(vcf_line)
    id += 1
