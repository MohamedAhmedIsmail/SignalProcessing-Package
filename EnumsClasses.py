from enum import Enum
class DiscreteOrContinuous(Enum):
    discrete=1
    continuous=0
    
class Operations(Enum):
    Add=0
    Subtract=1
    Multiply=2
    
class bitsOrLevels(Enum):
    bits=0
    levels=1
class SinOrCos(Enum):
    sin=0
    cos=1
    
class TypeOfNormalization(Enum):
    zeroToOne=0
    negativeOneToOne=1
    
class DFTOrIDFT(Enum):
    DFT=0
    IDFT=1
class PhaseAndAmplitude(Enum):
    Phase=0
    Amplitude=1
class DelayAdvance(Enum):
    Delay=0
    Advance=1
    fold=2
    notFold=3
class NormalizedOrNonNormalized(Enum):
    Normalized=0
    NonNormalized=1
    
    