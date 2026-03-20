{-|
Module      : 1JC3-Assign2.Assign_2.hs
Copyright   :  (c) William M. Farmer 2024
License     :  GPL (see the LICENSE file)
Maintainer  :  none
Stability   :  experimental
Portability :  portable

Description:
  Assignment 2 - McMaster CS 1JC3 2025

  Modified by W. M. Farmer 9 October 2025
-}
module Assign_2 where

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
-- Date: October 26, 2025
macid :: String
macid = "weic39"

type GaussianRat = (Rational,Rational)

{- -----------------------------------------------------------------
 - gaussReal
 - -----------------------------------------------------------------
 - Description:
 -   Extracts the coefficient of the real part
 -}
gaussReal :: GaussianRat -> Rational
gaussReal (a,b) = a

{- -----------------------------------------------------------------
 - gaussImag
 - -----------------------------------------------------------------
 - Description:
 -   Extracts the coefficent of the imaginary part
 -}
gaussImag :: GaussianRat -> Rational
gaussImag (a,b) = b

{- -----------------------------------------------------------------
 - gaussConj
 - -----------------------------------------------------------------
 - Description:
 -   negates the coefficient of the imaginary part
 -}
gaussConj :: GaussianRat -> GaussianRat
gaussConj (x,y) = (x,-y)

{- -----------------------------------------------------------------
 - gaussAdd
 - -----------------------------------------------------------------
 - Description:
 -   Adds 2 GaussianRats
 -}
gaussAdd :: GaussianRat -> GaussianRat -> GaussianRat
gaussAdd (a,b) (x,y) = (a + x, b + y)

{- -----------------------------------------------------------------
 - gaussMul
 - -----------------------------------------------------------------
 - Description:
 -   Multiplies 2 GaussianRats
 -}
gaussMul :: GaussianRat -> GaussianRat -> GaussianRat
gaussMul (a,b) (x,y) = (a*x - b*y, a*y + b*x)

{- -----------------------------------------------------------------
 - gaussRecip
 - -----------------------------------------------------------------
 - Description:
 -   Returns the reciprocal of a GaussianRat
 -}
gaussRecip :: GaussianRat -> GaussianRat
gaussRecip (0,0) = error "Undefined"
gaussRecip (a,b) = (a/(a*a + b*b),-(b/(a*a + b*b)))

{- -----------------------------------------------------------------
 - gaussNorm
 - -----------------------------------------------------------------
 - Description:
 -   Finds the norm of a GaussianRat
 -}
gaussNorm :: GaussianRat -> Rational
gaussNorm (a,b) = a*a + b*b

{- -----------------------------------------------------------------
 - gaussAddList
 - -----------------------------------------------------------------
 - Description:
 -   Adds up all GaussianRats in the list
 -}
gaussAddList :: [GaussianRat] -> GaussianRat
gaussAddList [] = (0,0)
gaussAddList (x:xs) = gaussAdd x (gaussAddList xs)

{- -----------------------------------------------------------------
 - gaussMulList
 - -----------------------------------------------------------------
 - Description:
 -   Multiplies all GaussianRats in the list
 -}
gaussMulList :: [GaussianRat] -> GaussianRat
gaussMulList [] = (1,0)
gaussMulList (x:xs) = gaussMul x (gaussMulList xs)

{- ------------------------------------------------------------------------
 - gaussCircle
 - ------------------------------------------------------------------------
 - Description:
 -   Forms a list of GaussianRats with a norm less than r
 -}
gaussCircle :: [GaussianRat] -> Rational -> [GaussianRat]
gaussCircle xs r = [x | x <- xs, gaussNorm x < r]

{-
  Function: gaussConj
  Test Case Number: 1
  Input: (123,-1.34)
  Expected Output: (123,1.34)
  Actual Output: (123 % 1,67 % 50)

  Function: gaussConj
  Test Case Number: 2
  Input: (12,57)
  Expected Output: (12,-57)
  Actual Output: (12 % 1,(-57) % 1)

  Function: gaussConj
  Test Case Number: 3
  Input: (1.329,127)
  Expected Output:(1.329,-127) 
  Actual Output: (1329 % 1000,(-127) % 1)
-------------------------------------------------
  Function: gaussAdd
  Test Case Number: 1
  Input: (-123,5.43) (4,89.57)
  Expected Output: (-119, 95)
  Actual Output: ((-119) % 1,95 % 1)

  Function: gaussAdd
  Test Case Number: 2
  Input: (056,35.500) (32,43)
  Expected Output: (88, 78.5) 
  Actual Output: (88 % 1,157 % 2)

  Function: gaussAdd
  Test Case Number: 3
  Input: (-4345,0) (345,0)
  Expected Output: (-4000,0)
  Actual Output: ((-4000) % 1,0 % 1)
-------------------------------------------------
  Function: gaussMul
  Test Case Number: 1
  Input: (3,4) (1,6)
  Expected Output: (-21,22)
  Actual Output: ((-21) % 1,22 % 1)

  Function: gaussMul
  Test Case Number: 2
  Input: (12345678,794) (123,987654)
  Expected Output: (734321118,12193258357074)
  Actual Output: (734321118 % 1,12193258357074 % 1)

  Function: gaussMul
  Test Case Number: 3
  Input: (0,0) (123,734)
  Expected Output: (0,0)
  Actual Output: (0 % 1,0 % 1)
-------------------------------------------------
  Function: gaussRecip
  Test Case Number: 1
  Input: (0,0)
  Expected Output: Error
  Actual Output: Error: Undefined

  Function: gaussRecip
  Test Case Number: 2
  Input: (3,4)
  Expected Output: (0.12, -0.16)
  Actual Output: (3 % 25,(-4) % 25)

  Function: gaussRecip
  Test Case Number: 3
  Input: (3,-4)
  Expected Output:(0.12, 0.16)
  Actual Output: (3 % 25,4 % 25)
-------------------------------------------------
  Function: gaussNorm
  Test Case Number: 1
  Input: (12,2)
  Expected Output: 148
  Actual Output: 148 % 1

  Function: gaussNorm
  Test Case Number: 2
  Input: (234.5,-6)
  Expected Output: 55026.25
  Actual Output: 220105 % 4

  Function: gaussNorm
  Test Case Number: 3
  Input: (-3,9)
  Expected Output: 90 
  Actual Output: 90 % 1
-------------------------------------------------
  Function: gaussAddList
  Test Case Number: 1
  Input: []
  Expected Output: (0,0)
  Actual Output: (0 % 1, 0 % 1)

  Function: gaussAddList
  Test Case Number: 3
  Input: [(12,2),(-1.23,8),(1.48,-4),(-5,0.243),(61.974,3)]
  Expected Output: (69.224, 9.243)
  Actual Output: (8653 % 125,9243 % 1000)

  Function: gaussAddList
  Test Case Number: 2
  Input: [(12,2),(1,8),(13,4),(5,7),(6,3)]
  Expected Output: (37,24)
  Actual Output: (37 % 1,24 % 1)
-------------------------------------------------
  Function: gaussMulList
  Test Case Number: 1
  Input: []
  Expected Output: (1,0) 
  Actual Output: (1 % 1,0 % 1)

  Function: gaussMulList
  Test Case Number: 2
  Input: [(3,4),(1,6)]
  Expected Output: (-21,22)
  Actual Output: ((-21) % 1,22 % 1)

  Function: gaussMulList
  Test Case Number: 3
  Input: [(3,4),(1,6),(2,5)]
  Expected Output: (-152,-61)
  Actual Output: ((-152) % 1,(-61) % 1)
-------------------------------------------------
  Function: gaussCircle
  Test Case Number: 1 
  Input: [] 0
  Expected Output: []
  Actual Output: []
  
  Function: gaussCircle
  Test Case Number: 2
  Input: [(3,4),(6,8),(5,12)] 100
  Expected Output: [3,4]
  Actual Output: [(3 % 1,4 % 1)]
  
  Function: gaussCircle
  Test Case Number: 3
  Input: [(3,4),(12,5),(8,11),(6,8),(15,15)] 170
  Expected Output: [(3,4),(12,5),(6,8)]
  Actual Output: [(3 % 1,4 % 1),(12 % 1,5 % 1),(6 % 1,8 % 1)]
-}