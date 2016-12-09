/**
Get SNP location and SNPs in format
TlocationC, GlocationA

Type - Type of change
Ref  - Reference value
Allele - Consensus Value
Crc - Coding region change

--- Author: George Dzavashvili
--- Email: dzavashviligeorge@gmail.com
--- Twitter: @redpix_
@customFunction
*/
function FormatSNP(Type, Ref, Allele, Crc) {
  if (Type === "SNV") {
    return ProcessSNP(Ref, Allele, Crc);
  }
  else if (Type === "Insertion"){
    return ProcessInsertion(Ref, Allele, Crc);
  }
  else if (Type === "Deletion"){
    return ProcessDeletion(Ref, Allele, Crc);
  }
  else{
    return "Unknown";
  }
}

/**
Process Insertion alone for the sake of readability and structure
@customFunction
*/
function ProcessDeletion(Ref, Allele, Crc){
  var final = "";
  final += Ref + "del";
  if (Crc){
      // Add reference location
      var coded = Crc.split(":c.")[1];
      if(/\[+/.test(coded)){
        final += "_UNKNOWN";
      }else{
        var extracted = "";
        for (var i = 0; i < coded.length; i++){
          if (!isNaN(parseInt(coded[i], 10))){
            // Number
            extracted += coded[i];
          }else{
            break;
          }
        }
        var f = parseInt(extracted, 10);
        final += f.toString();
      }
  }
  return final;
}

/**
Process Insertion alone for the sake of readability and structure
@customFunction
*/
function ProcessInsertion(Ref, Allele, Crc){
  var final = "";
  final += Allele + "ins";
  if (Crc){
      // Add reference location
      var coded = Crc.split(":c.")[1];
      if(/\[+/.test(coded)){
        final += "_UNKNOWN";
      }else{
        var extractedF = coded.split("_")[1];
        var extracted = "";
        
        for (var i = 0; i < extractedF.length; i++){
          if (!isNaN(parseInt(extractedF[i], 10))){
            // Number
            extracted += extractedF[i];
          }else{
            break;
          }
        }
        var f = parseInt(extracted, 10);
        final += f.toString();
      }
  }
  return final;
}

/**
Process SNP alone for the sake of readability and structure
@customFunction
*/
function ProcessSNP(Ref, Allele, Crc){
  var final = "";
  // Add Reference value
  final += Ref;
  // Get Location
  if (Crc){
    // Set the formatting
    var coded = Crc.split(":c.")[1];
    var extracted = "";
    for (var i = 0; i < coded.length; i++){
      if (!isNaN(parseInt(coded[i], 10))){
    		extracted += coded[i];
      }else{
    		break;
      }
    }
    var f = parseInt(extracted, 10);
    final += f.toString();
  }
  else{
    // Set just A>T
    final += ">";
  }
  final += Allele;
  return final;
}

/**
Determine Codon Position
fd - Formatted Data
@customFunction
*/
function CodonPos(fd){
  var final = "";
  var seq = false;
  for (var i = 0; i < fd.length; i++){
    if (!isNaN(parseInt(fd[i], 10))){
      if(!seq)
        seq = true;
      final += fd[i];
    }else{
      if (seq)
        break;
    }
  }
  var n = parseInt(final, 10);
  if (!isNaN(n)){
    var m = n % 3;
    if (m === 0){
      return 3;
    }else{
      return m;
    }
  }else{
    return "";
  }
}

/**
Extract Amino Acid Change Information if possible
aac - Amino acid change
@customFunction
*/
function AminoAcidChange(aac){
  var final = "";
  if (aac){
    var coded = aac.split(":p.")[1];
    if(/\[+/.test(coded)){
      final += "UNKNOWN";
    }else{
      final += coded;
    }
  }
  return final;
}