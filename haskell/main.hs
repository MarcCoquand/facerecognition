import System.Random
import Data.List
import Data.Ord
import System.Environment
import Data.Char
import Data.List.Split

-- ------------------------------------------------------------------------------
-- | TYPE DEFINITIONS AND GLOBALS

type Ans  = Integer
type Pix  = [Integer]
type Img  = [(Pix, Ans)]

--   Perceptron consist of id from 1-4 and it's weights
type Perceptron = (Integer, [Integer])

-- ------------------------------------------------------------------------------
-- | PERCEPTRON
-- | Perceptron represents a perceptron in the network. A perceptron
-- | represent one of the four feelings specified in the TYPE field.
-- | It reacts to an input image with a response based on it's training.

-- | Process the image with a perceptron
process :: Perceptron -> Img -> Integer
process _ []      = 0
process (_,[]) _	= 0
process p i = sum (map sum (q p i))
				where
				q :: Perceptron -> Img -> [[Integer]]
				q _ []		 = []
				q (_,[]) _ = []
				q p (i:is) = ((zipWith (*) (fst i) (snd p))):(q p is)


-- | Generate weights of length l
weightGen :: Int -> StdGen -> [Float]
weightGen n = take n . unfoldr (Just . random)

-- | Update the weights with a delta error
weightUpd :: [Float] -> [Float] -> [Float]
weightUpd fw fd = zipWith (+) fw fd

-- | Activation given a sum of weighted input
computeAct :: Float -> Float
computeAct f = 1/(1 + exp (f))

-- ------------------------------------------------------------------------------
-- | TUTOR

{-train :: [Perceptron] -> img -> [Perceptron]-}

-- | Calculate mean square error and check if less than a threshold t, suggested
--   threshold is 0.01
accurate :: [Float] -> Float -> Bool
accurate [] _ = False 
accurate f t  = mse < t 
								where
								mse = (sum (map (\x -> x**2) f))/2 

desired :: (Pix, Ans) -> Perceptron -> Integer
desired i p = if (snd i) == (fst p) then 1 else 0

deltaWeight :: Pix -> Float -> Float -> [Float]
deltaWeight [] _ _ = []
deltaWeight p l f = map (\x -> x*l*f) p 

-- ------------------------------------------------------------------------------
-- | EXAMINER
-- | Examiner is a class that, provided a set of trained neurons and
-- | test images, examines the training results of the network

examine :: Img -> ((Pix, Ans) -> String) -> [String]
examine [] _     = []
examine (i:is) f = f i:examine is f

-- | Shows an image to all of the perceptrons and returns the largest
--   activation from the network. 
exposeP :: [Perceptron] -> Img -> Integer -> Integer
exposeP [] _ i = i
exposeP (p:ps) i c  = let
				proc = process p i
				new = if c>proc then c else (fst p)
				in exposeP ps i new

formatOutput :: Integer ->  Integer -> String
formatOutput img guess = "Gussing: " ++ show guess ++ ". Right answer: " ++ 
													show img

-- ------------------------------------------------------------------------------
-- | IMAGE
-- | Image represents an image that holds a list of pixels, id, and what
-- | facial expression the image represents.

-- | Take out all integers in string and convert to [Integer]
toIntL :: String -> [Integer]
toIntL [] = []
toIntL s  = map (read::String->Integer) (splitOn " " s)

-- | Filter noise in image, i.e. all values less than 3.
noiseF :: Img -> Img
noiseF []     = []
noiseF (i:is) = (map (\x -> if x<3 then 0 else x) (fst i), (snd i)):noiseF is

-- | Parse the image txt file and convert it to a matrix of strings
--   to later be converted with toIntL
isName :: String -> Bool
isName (ms:_) = not $ isDigit ms
isName []     = True

fAux :: [[String]] -> [String] -> [String] -> [[String]]
fAux acc us [] = reverse (reverse us:acc)
fAux acc us (s:ss) 
  | isName s  = fAux (us:acc) [] ss
  | otherwise = fAux acc (s:us) ss

-- | Takes lines of answers, removes the first word and returns the last one
--   that should be a digit
pAns :: [String] -> [Ans]
pAns [] = []
pAns (s@(ms:_):as)  
  | ms == '#' = (pAns as)
  | otherwise = (read (last (splitOn " " s))):(pAns as)

-- ------------------------------------------------------------------------------
-- | MAIN

main :: IO ()
main = do 
  [p,a] <- getArgs
  pF <- readFile p
  pA <- readFile a
  seed <- newStdGen
	-- | Read both files and parse them, create a list of img, I.e. a face matching
	--   an answer
  let i  = zip (map concat (filter (not . null)  
								(map (map toIntL) (fAux [] [] (lines pF))))) (pAns (lines pA))
      iF = noiseF i
  putStrLn pF
