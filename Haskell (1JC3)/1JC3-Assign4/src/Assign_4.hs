{-# LANGUAGE InstanceSigs #-}
{-|
Module      : 1JC3-Assign4/src/Assign_4.hs
Copyright   : (c) William M. Farmer 2025
License     : GPL (see the LICENSE file)
Maintainer  : none
Stability   : experimental
Portability : portable
Description : Assignment 4 - McMaster CS 1JC3 2025
-}
module Assign_4 where

import Test.QuickCheck

--------------------------------------------------------------------------------
-- INSTRUCTIONS              README!!!
--------------------------------------------------------------------------------
-- 1) DO NOT DELETE/ALTER ANY CODE ABOVE THESE INSTRUCTIONS
-- 2) DO NOT REMOVE / ALTER TYPE DECLARATIONS (I.E THE LINE WITH THE :: ABOUT
--    THE FUNCTION DECLARATION). IF YOU ARE UNABLE TO COMPLETE A FUNCTION, LEAVE
--    IT'S ORIGINAL IMPLEMENTATION (I.E. THROW AN ERROR)
-- 3) MAKE SURE THE PROJECT COMPILES (I.E. RUN `stack build` AND MAKE SURE THERE
--    ARE NO ERRORS) BEFORE SUBMITTING. FAILURE TO DO SO WILL RESULT IN A MARK
--    OF 0!
-- 4) REPLACE macid = "TODO" WITH YOUR ACTUAL MACID (EX. IF YOUR MACID IS
--    "jim123" THEN `macid = "jim123"`). REMEMBER THAT YOUR MACID IS THE FIRST
--    PART OF YOUR SCHOOL EMAIL (I.E. IF YOUR EMAIL IS "jim123@mcmaster.ca",
--    THEN YOUR MACID IS "jim123"). FAILURE TO DO SO WILL RESULT IN A MARK OF 0!
--------------------------------------------------------------------------------

-- Name: Colin Wei
-- Date: 02/12/2025
macid :: String
macid = "weic39"

{- --------------------------------------------------------------------
 - Datatype: MathExpr
 - --------------------------------------------------------------------
 - Description: An Abstract Syntax Tree (AST) for encoding mathematical
 -              expressions
 - Example: The expression
 -            (2*X + 1) ^ 3
 -          can be encoded as
 -             Power (Sum (Prod (Coef 2) X) (Coef 1)) 3
 -
 - --------------------------------------------------------------------
 -}
data MathExpr a =
    X
  | Coef  a
  | Sum   (MathExpr a) (MathExpr a)
  | Prod  (MathExpr a) (MathExpr a)
  | Quot  (MathExpr a) (MathExpr a)
  | Power (MathExpr a) Integer
  | Abs   (MathExpr a)
  | Exp   (MathExpr a)
  | Log   (MathExpr a)
  deriving (Eq,Show,Read)

{- -----------------------------------------------------------------
 - eval
 - -----------------------------------------------------------------
 - Description:
 -    Evaluates an expression by substituting any instance of X with v
 -}
eval :: (Floating a, Eq a) => MathExpr a -> a -> a
eval X v = v
eval (Coef x) v = x
eval (Sum x y) v = eval x v + eval y v
eval (Prod x y) v = eval x v * eval y v
eval (Quot x y) v = eval x v / eval y v
eval (Power x i) v = eval x v ^^ i
eval (Abs x) v = abs (eval x v)
eval (Exp x) v = exp (eval x v)
eval (Log x) v = log (eval x v)

{- -----------------------------------------------------------------
 - instance Num a => Num (MathExpr a)
 - -----------------------------------------------------------------
 - Description:
 -    Converts operators into their MathExpr equivalents
 -}
instance Num a => Num (MathExpr a) where
  (+) :: Num a => MathExpr a -> MathExpr a -> MathExpr a
  x + y         = Sum x y
  (*) :: Num a => MathExpr a -> MathExpr a -> MathExpr a
  x * y         = Prod x y
  negate :: Num a => MathExpr a -> MathExpr a
  negate x      = Prod x (Coef (-1))
  abs :: Num a => MathExpr a -> MathExpr a
  abs x         = Abs x
  fromInteger :: Num a => Integer -> MathExpr a
  fromInteger i = Coef(fromInteger i)
  signum :: Num a => MathExpr a -> MathExpr a
  signum _      = error "signum is left un-implemented"

{- -----------------------------------------------------------------
 - instance Fractional a => Fractional (MathExpr a)
 - -----------------------------------------------------------------
 - Description:
 -    Expresses Fractionals in a MathExpr-compatible form
 -}
instance Fractional a => Fractional (MathExpr a) where
  e1 / e2        = Quot e1 e2
  fromRational e = Coef(fromRational e)

{- -----------------------------------------------------------------
 - instance Floating a => Floating (MathExpr a)
 - -----------------------------------------------------------------
 - Description:
 -    Changes various expressions into their MathExpr equivalents
 -}
instance Floating a => Floating (MathExpr a) where
  pi :: Floating a => MathExpr a
  pi      = Coef pi
  exp :: Floating a => MathExpr a -> MathExpr a
  exp     = Exp
  log :: Floating a => MathExpr a -> MathExpr a
  log     = Log
  sin   _ = error "sin is left un-implemented"
  cos   _ = error "cos is left un-implemented"
  tan   _ = error "cos is left un-implemented"
  asin  _ = error "asin is left un-implemented"
  acos  _ = error "acos is left un-implemented"
  atan  _ = error "atan is left un-implemented"
  sinh  _ = error "sinh is left un-implemented"
  cosh  _ = error "cosh is left un-implemented"
  tanh  _ = error "tanh is left un-implemented"
  asinh _ = error "asinh is left un-implemented"
  acosh _ = error "acosh is left un-implemented"
  atanh _ = error "atanh is left un-implemented"
  sqrt  _ = error "sqrt is left un-implemented"

{- -----------------------------------------------------------------
 - diff
 - -----------------------------------------------------------------
 - Description:
 -    Differentiates MathExprs in accordance with differentiation rules
 -}
diff :: (Floating a, Eq a) => MathExpr a -> MathExpr a
diff X = 1
diff (Coef a) = 0
diff (Sum x y) = diff x + diff y
diff (Prod x y) = diff x * y + x * diff y
diff (Quot x y) = Quot (Sum (diff x * y) (negate x * diff y))  (Power y 2)
diff (Power x n) = fromInteger n * Power x (n-1) * diff x
diff (Abs x) = Prod (Quot x (Abs x)) (diff x)
diff (Exp x) = Prod (diff x) (Exp x)
diff (Log x) = Quot (diff x) x

{- -----------------------------------------------------------------
 - prettyPrint
 - -----------------------------------------------------------------
 - Description: Outputs a visual representation of MathExprs

 -}
prettyPrint :: (Show a) => MathExpr a -> String
prettyPrint (Coef a) = show a
prettyPrint X = "x"
prettyPrint (Sum x y) = "(" ++ prettyPrint x ++ " + " ++ prettyPrint y ++ ")"
prettyPrint (Prod x y) = "(" ++ prettyPrint x ++ " * " ++ prettyPrint y ++ ")"
prettyPrint (Quot x y) = "(" ++ prettyPrint x ++ " / " ++ prettyPrint y ++ ")"
prettyPrint (Power x y) = "(" ++ prettyPrint x ++ ") ^ (" ++ show y ++ ")"
prettyPrint (Abs x) = "abs(" ++ prettyPrint x ++ ")"
prettyPrint (Exp x) = "e^(" ++ prettyPrint x ++ ")"
prettyPrint (Log x) = "log(" ++ prettyPrint x ++ ")"

{- -----------------------------------------------------------------
 - Test cases for eval, diff, and prettyPrint
 - -----------------------------------------------------------------
Function: eval
- Test Case Number: 1
- Input: Abs(Sum Power(X 2) (Coef (-4)) )
- Expected Output: 3.0
- Actual Output: 3.0
- Rationale: Tests Abs, Sum, Power, and negative coefficients.

- Test Case Number: 2
- Input: Quot (Exp (Prod (Coef 0) X)) (Log X)
- Expected Output: 0.0
- Actual Output: 0.0
- Rationale: 
  - Shows that evaluation displays a "special number (Infinity to be exact)"
  - Tests Quot, Prod, exp, and log 

- Test Case Number: 3
- Input: 
eval (Sum (Prod (Coef 7) (Power X 2) (Sum (Prod (Coef 6) X) (Coef (0.2)))) 12.1
- Expected Output: 1097.67
- Actual Output: 1097.6699999999998 (within 1e-4 tolerance)
- Rationale: Computatation of a degree 2 function

Function: diff
- Test Case Number: 1
- Input: Quot (Coef 1) X
- Expected Output: 
Quot (
  Sum (Prod (Coef 0.0) X) (Prod (Prod (Coef 1.0) (Coef (-1.0))) (Coef 1.0))
) (Power X 2)
- Actual Output: 
Quot (
  Sum (Prod (Coef 0.0) X) (Prod (Prod (Coef 1.0) (Coef (-1.0))) (Coef 1.0))
) (Power X 2)
- Rationale: I was experiencing trouble implementing the quotient product. 
    Also shows negate in action

- Test Case Number: 2
- Input: Sum (Prod (Coef 2) (Power X 2)) (Exp X)
- Expected Output: 
  Sum (  
    Sum 
      (Prod (Coef 0.0) (Power X 2)) 
      (Prod (Coef 2.0) (Prod (Prod (Coef 2.0) (Power X 1)) (Coef 1.0)))
  ) 
  (Prod (Coef 1.0) (Exp X))
- Actual Output:
  Sum (  
    Sum 
      (Prod (Coef 0.0) (Power X 2)) 
      (Prod (Coef 2.0) (Prod (Prod (Coef 2.0) (Power X 1)) (Coef 1.0)))
  )
  (Prod (Coef 1.0) (Exp X)) 
- Rationale: tests exp, addition and multiplication ruless

- Test Case Number: 3
- Input: Log (Power (Prod (Coef 2) X) 2)
- Expected Output: 
  Quot (Sum (Prod (Prod (Coef 2.0) (Power X 1)) (Coef 1.0)) (Coef 0.0)) 
      (Sum (Power X 2) (Coef 1.0))
- Actual Output: 
  Quot (Sum (Prod (Prod (Coef 2.0) (Power X 1)) (Coef 1.0)) (Coef 0.0)) 
      (Sum (Power X 2) (Coef 1.0))
- Rationale: tests log rule

Function: prettyPrint
- Test Case Number: 1
- Input: Abs(Sum (Power X 2) (Coef (-4)) )
- Expected Output: abs(((x) ^ (2) + -4))
- Actual Output: abs(((x) ^ (2) + -4))
- Rationale: tests abs, sum, power, coef

- Test Case Number: 2
- Input: Quot (Exp (Prod (Coef 0) X)) (Log X)
- Expected Output: "(e^((0 * x)) / log(x))"
- Actual Output: "(e^((0 * x)) / log(x))"
- Rationale: tests exp, log, quot

- Test Case Number: 3
- Input: Sum (Prod (Coef 7) (Power X 2)) (Sum (Prod (Coef 6) X) (Coef 20))
- Expected Output: ((7 * (x) ^ (2)) + ((6 * x) + 20))
- Actual Output: ((7 * (x) ^ (2)) + ((6 * x) + 20))
- Rationale:
    Printing of a degree 2 expression
    tests prod
 -}

{- -----------------------------------------------------------------
 - QuickCheck cases for eval and diff
 - -----------------------------------------------------------------
 -}
{- EXAMPLE
 - Function: eval
 - Property: eval (Sum (Coef x) X) y is correct for all x,y
 - Actual Test Result: Pass
 - Code:
-}

evalProp0 :: (Float,Float) -> Bool
evalProp0 (x,y) = (x + y) =~ eval (Sum (Coef x) X) y

runEvalProp0 :: IO ()
runEvalProp0 = quickCheck evalProp0

(=~) :: (Floating a,Ord a) => a -> a -> Bool
x =~ y = abs (x - y) <= 1e-4

{- 
 - Function: eval
 - Property: eval (Exp (Log (Sum (Coef 1) (Abs X)))) y is correct for all y
 - Actual Test Result: True
 - Code:
-}

evalProp1 :: Float -> Bool
evalProp1 y = (abs y + 1) =~ eval (Exp (Log (Sum (Coef 1) (Abs X)))) y

runEvalProp1 :: IO ()
runEvalProp1 = quickCheck evalProp1

{- 
 - Function: eval
 - Property: 
  eval (Sum (Prod (Coef a) (Power X 2)) (Sum (Prod (Coef b) X) (Coef c))) x
  is correct for all a b c x
 - Actual Test Result: True
 - Code:
-}

evalProp2 :: (Double,Double,Double,Double) -> Bool
evalProp2 (a,b,c,x) = (a * x^^2 + b*x + c) =~ 
  eval (Sum (Prod (Coef a) (Power X 2)) (Sum (Prod (Coef b) X) (Coef c)) ) x

runEvalProp2 :: IO ()
runEvalProp2 = quickCheck evalProp2


{- 
 - Function: diff
 - Property: diff (Abs X) is correct for all X (undefined when 0)
 - Actual Test Result: True
 - Code:
-}

diffProp1 :: Float -> Bool
diffProp1 y
  | y == 0 = (0/0) /= eval (diff (Abs X)) y
  | otherwise = (y /abs y) =~ eval (diff (Abs X)) y

runDiffProp1 :: IO ()
runDiffProp1 = quickCheck diffProp1

{- 
 - Function: diff
 - Property: 
    diff (Power (Sum (Prod (Coef x) X) (Coef y)) 2) is correct for all x,y
 - Actual Test Result: True
 - Code:
-}

diffProp2 :: (Float,Float,Float) -> Bool
diffProp2 (x,y,z) = (2*x*(x*z+y)) =~ 
  eval (diff (Power (Sum (Prod (Coef x) X) (Coef y)) 2)) z

runDiffProp2 :: IO ()
runDiffProp2 = quickCheck diffProp2