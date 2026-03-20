{-|
Module      : 1JC3-Assign3.Assign_3.hs
Copyright   :  (c) William M. Farmer 2025
License     :  GPL (see the LICENSE file)
Maintainer  :  none
Stability   :  experimental
Portability :  portable

Description:
  Assignment 3 - McMaster CS 1JC3 2025
-}
module Assign_3 where

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
-- Date: November 16 2025
macid :: String
macid = "weic39"

{- -----------------------------------------------------------------
 - LambdaTerm algebraic type
 - -----------------------------------------------------------------
 -}

data LambdaTerm =
    Var Integer
  | FunApp LambdaTerm LambdaTerm
  | FunAbs Integer LambdaTerm
  deriving (Eq,Show)

{- -----------------------------------------------------------------
 - isFreeIn
 - -----------------------------------------------------------------
 - Description:
 -  True if at least one free instance of variable v is in the other LambdaTerm
 -}
isFreeIn :: LambdaTerm -> LambdaTerm -> Bool
isFreeIn (Var v) (FunApp m n) = isFreeIn (Var v) m || isFreeIn (Var v) n
isFreeIn (Var v) (FunAbs w n)
  |Var v == Var w = False
  |otherwise = isFreeIn (Var v) n
isFreeIn (Var v) (Var x) = Var v == Var x
isFreeIn _ _ = False

{- -----------------------------------------------------------------
 - freshVarList
 - -----------------------------------------------------------------
 - Description:
 -    Returns integer not present in the list of LambdaTerms
 -}
freshVarList :: [LambdaTerm] -> Integer
freshVarList [] = 1
freshVarList ms = 
  let
    dissect :: LambdaTerm -> Integer
    dissect (FunAbs x o) = max x (dissect o)
    dissect (FunApp m n) = max (dissect m) (dissect n)
    dissect (Var y) = y
  in 
    maximum(map dissect ms) + 1

{- -----------------------------------------------------------------
 - sub
 - -----------------------------------------------------------------
 - Description:
 -    Substitutes term 2 in the position of term 1 within term 3

rework case 1

sub (Var 1) (Var 2) (FunAbs 1 (FunApp(Var 1)(Var 2)) )

sub (Var 3) (Var 2) (FunAbs 1 (FunApp(Var 1)(Var 2)) )

sub (FunAbs 1 (Var 3)) (Var 2) (FunAbs 1 (Var 4))

sub (FunAbs 1 (Var 3)) (Var 4) (FunAbs 1 (Var 4))

 -}
sub :: LambdaTerm -> LambdaTerm -> LambdaTerm -> LambdaTerm
sub m (Var x) (FunAbs y n)
  |Var x == Var y = FunAbs y n
  |not (isFreeIn (Var y) m) = FunAbs y (sub m (Var x) n)
  |otherwise =
    let 
      y' = freshVarList[m, Var x, Var y, n]
    in FunAbs y' (sub m (Var x) (sub (Var y') (Var y) n)) 
sub m (Var x) (FunApp n o) = FunApp (sub m (Var x) n) (sub m (Var x) o)
sub m (Var x) n
  |n == Var x = m
  |otherwise = n
sub m _ n = n

{- -----------------------------------------------------------------
 - isRedex
 - -----------------------------------------------------------------
 - Description:
 -    Checks whether the term is a redex
 -}
isRedex :: LambdaTerm -> Bool
isRedex (FunApp (FunAbs x n) m) = True
isRedex _ = False

{- -----------------------------------------------------------------
 - betaRed
 - -----------------------------------------------------------------
 - Description:
 -    Beta reduces the term if possible
 -}
betaRed :: LambdaTerm -> LambdaTerm
betaRed (FunApp (FunAbs x n) m) = sub m (Var x) n
betaRed m = m

{- -----------------------------------------------------------------
 - normOrdRed
 - -----------------------------------------------------------------
 - Description:
 -    Normal order reduces a lambda term to a normal form
 -}
normOrdRed :: LambdaTerm -> LambdaTerm
normOrdRed (Var i) = Var i
normOrdRed (FunApp m n) =
  let
    headBetaRed o =
      case o of
        (Var i) -> Var i
        (FunApp p q) ->
          case headBetaRed p of
            (FunAbs i p) -> headBetaRed (betaRed (FunApp (FunAbs i p) q))
            p'          -> FunApp p' q
        (FunAbs i p) -> (FunAbs i p)
    in case headBetaRed m of
      FunAbs i p -> normOrdRed (betaRed (FunApp (FunAbs i p) n))
      m'         -> FunApp (normOrdRed m') (normOrdRed n)
normOrdRed (FunAbs i m) = FunAbs i (normOrdRed m)

{- -----------------------------------------------------------------
 - prettyPrint
 - -----------------------------------------------------------------
 - Description:
 -    Represents a lambdaTerm within a String
 -}
prettyPrint :: LambdaTerm -> String
prettyPrint (FunApp m n) = "(" ++  prettyPrint m ++ " " ++ prettyPrint n ++ ")"
prettyPrint (FunAbs x o) = "(lambda x"++ show x ++" . "++ prettyPrint o ++")"
prettyPrint (Var y) = "x" ++ show y

{-
Function: isFreeIn
  Test Case Number: 1
  Input: (Var 1) (FunApp (Var 2) (FunAbs 3 (FunApp(Var 1) (Var 2)) ) )
  Expected Output: True
  Actual Output: True

  Test Case Number: 2
  Input: (Var 3) (FunApp (Var 2) (FunAbs 3 (FunApp(Var 1) (Var 2)) ) )
  Expected Output: False
  Actual Output: False

  Test Case Number: 3
  Input: (Var 2) (FunAbs 2 (Var 2))
  Expected Output: False
  Actual Output: False

Function: freshVarList
  Test Case Number: 1
  Input: []
  Expected Output: 1
  Actual Output: 1

  Test Case Number: 2
  Input: [FunApp (FunAbs 4 (FunAbs 1 (Var 4))) (FunAbs 1 (Var 3)), (Var 2)]
  Expected Output: 5
  Actual Output: 5

  Test Case Number: 3
  Input: [(FunAbs 1 (Var 3)), (Var 4), (FunAbs 1 (Var 4)), (Var 7)]
  Expected Output: 8
  Actual Output: 8

Function: Sub
  Test Case Number: 1
  Input: (FunAbs 1 (Var 3)) (Var 4) (FunAbs 1 (Var 4))
  Expected Output: FunAbs 1 (FunAbs 1 (Var 3))
  Actual Output: FunAbs 1 (FunAbs 1 (Var 3))

  Test Case Number: 2
  Input: (FunAbs 1 (Var 3)) (Var 2) (FunAbs 1 (Var 4))
  Expected Output: FunAbs 1 (Var 4)
  Actual Output: FunAbs 1 (Var 4)

  Test Case Number: 3
  Input: (Var 1) (Var 2) (FunAbs 1 (FunApp(Var 1)(Var 2)))
  Expected Output: FunAbs 3 (FunApp (Var 3) (Var 1))
  Actual Output FunAbs 3 (FunApp (Var 3) (Var 1))

Function: isRedex
  Test Case Number: 1
  Input: (FunApp (FunAbs 4 (FunAbs 1 (Var 4))) (FunAbs 1 (Var 3)))
  Expected Output: True
  Actual Output: True

  Test Case Number: 2
  Input: (FunApp (Var 1) (Var 2))
  Expected Output: False
  Actual Output: False

  Test Case Number: 3
  Input: (FunApp (Var 1) (FunAbs 2 (Var 3)))
  Expected Output: False
  Actual Output: False

Function: betaRed
  Test Case Number: 1
  Input: (FunApp (FunAbs 4 (FunAbs 1 (Var 4))) (FunAbs 1 (Var 3)))
  Expected Output: FunAbs 1 (FunAbs 1 (Var 3))
  Actual Output: FunAbs 1 (FunAbs 1 (Var 3))

  Test Case Number: 2
  Input: FunApp (Var 4) (FunAbs 1 (Var 3))
  Expected Output: FunApp (Var 4) (FunAbs 1 (Var 3))
  Actual Output: FunApp (Var 4) (FunAbs 1 (Var 3))

  Test Case Number: 3
  Input: (FunApp (FunAbs 4 (FunApp (Var 4)(Var 4))) (Var 3))
  Expected Output: FunApp (Var 3) (Var 3)
  Actual Output: FunApp (Var 3) (Var 3)

Function: normOrdRed
  Test Case Number: 1
  Input: (FunApp (FunAbs 4 (FunAbs 1 (Var 4))) (FunAbs 1 (Var 3)))
  Expected Output: FunAbs 1 (FunAbs 1 (Var 3))
  Actual Output: FunAbs 1 (FunAbs 1 (Var 3))

  Test Case Number: 2
  Input: (FunApp (Var 4) (FunAbs 1 (Var 3)))
  Expected Output: (FunApp (Var 4) (FunAbs 1 (Var 3)))
  Actual Output: (FunApp (Var 4) (FunAbs 1 (Var 3)))

  Test Case Number: 3
  Input: FunApp (
          FunAbs 4 (FunApp (Var 4)(Var 4))) 
          ((FunApp (FunAbs 1 (FunAbs 2 (Var 1)) ) (Var 2))
        )
  Expected Output: Var 2
  Actual Output: Var 2

Function: prettyPrint 
  Test Case Number: 1
  Input: (FunApp (FunAbs 4 (FunAbs 1 (Var 4))) (FunAbs 1 (Var 3)))
  Expected Output: "((lambda x4 . (lambda x1 . x4)) (lambda x1 . x3))"
  Actual Output: "((lambda x4 . (lambda x1 . x4)) (lambda x1 . x3))"

  Test Case Number: 2
  Input: (FunApp (Var 2) (FunAbs 3 (FunApp(Var 1) (Var 2))))
  Expected Output: "(x2 (lambda x3 . (x1 x2)))"
  Actual Output: "(x2 (lambda x3 . (x1 x2)))"

  Test Case Number: 3
  Input: (FunApp (FunAbs 1 (FunAbs 2 (Var 1)) ) (Var 2))
  Expected Output: "((lambda x1 . (lambda x2 . x1)) x2)"
  Actual Output: "((lambda x1 . (lambda x2 . x1)) x2)"
-}