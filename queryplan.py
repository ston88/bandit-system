import xml.etree.ElementTree as ET

class QueryPlan():

    def __init__(self, xml_string):
        self.predicates = []
        self.estimated_rows = 0
        self.estimated_sub_tree_cost = 0 

        root = ET.fromstring(xml_string)
        predicates = root.findall('.//{http://schemas.microsoft.com/sqlserver/2004/07/showplan}Predicate')
        for predicate in predicates:
            for column_reference in predicate.findall('.//{http://schemas.microsoft.com/sqlserver/2004/07/showplan}ColumnReference'):
                if column_reference.attrib.get('Table') is not None and column_reference.attrib.get('Column') is not None:
                    column = column_reference.attrib.get('Table') + "." + column_reference.attrib.get('Column')
                    if column not in self.predicates:
                        self.predicates.append(column)

        stmt_simple = root.find('.//{http://schemas.microsoft.com/sqlserver/2004/07/showplan}StmtSimple')
        self.estimated_rows = stmt_simple.attrib.get('StatementEstRows')
        self.estimated_sub_tree_cost = stmt_simple.attrib.get('StatementSubTreeCost')

# For Testing
qp = QueryPlan('''<ShowPlanXML xmlns="http://schemas.microsoft.com/sqlserver/2004/07/showplan" Version="1.6" Build="14.0.2002.14">
  <BatchSequence>
    <Batch>
      <Statements>
        <StmtSimple StatementText="SELECT * FROM dbo.NATION WHERE N_NAME = N_NAME AND N_NAME LIKE (SELECT TOP 1 '%A%' FROM dbo.NATION)" StatementId="1" StatementCompId="1" StatementType="SELECT" RetrievedFromCache="true" StatementSubTreeCost="0.0245705" StatementEstRows="2.25" SecurityPolicyApplied="false" StatementOptmLevel="FULL" QueryHash="0x4ACBFC9697C70884" QueryPlanHash="0xBE52623CD4CD4272" StatementOptmEarlyAbortReason="GoodEnoughPlanFound" CardinalityEstimationModelVersion="140">
          <StatementSetOptions QUOTED_IDENTIFIER="true" ARITHABORT="true" CONCAT_NULL_YIELDS_NULL="true" ANSI_NULLS="true" ANSI_PADDING="true" ANSI_WARNINGS="true" NUMERIC_ROUNDABORT="false" />
          <QueryPlan CachedPlanSize="40" CompileTime="6" CompileCPU="6" CompileMemory="432">
            <MemoryGrantInfo SerialRequiredMemory="0" SerialDesiredMemory="0" />
            <OptimizerHardwareDependentProperties EstimatedAvailableMemoryGrant="416282" EstimatedPagesCached="104070" EstimatedAvailableDegreeOfParallelism="2" MaxCompileMemory="8051808" />
            <RelOp NodeId="0" PhysicalOp="Filter" LogicalOp="Filter" EstimateRows="2.25" EstimateIO="0" EstimateCPU="3.7e-005" AvgRowSize="120" EstimatedTotalSubtreeCost="0.0245705" Parallel="0" EstimateRebinds="0" EstimateRewinds="0" EstimatedExecutionMode="Row">
              <OutputList>
                <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NATIONKEY" />
                <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_REGIONKEY" />
                <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_COMMENT" />
              </OutputList>
              <Filter StartupExpression="0">
                <RelOp NodeId="1" PhysicalOp="Nested Loops" LogicalOp="Left Outer Join" EstimateRows="25" EstimateIO="0" EstimateCPU="0.0001045" AvgRowSize="132" EstimatedTotalSubtreeCost="0.0245335" Parallel="0" EstimateRebinds="0" EstimateRewinds="0" EstimatedExecutionMode="Row">
                  <OutputList>
                    <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NATIONKEY" />
                    <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                    <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_REGIONKEY" />
                    <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_COMMENT" />
                    <ColumnReference Column="Expr1006" />
                    <ColumnReference Column="Expr1010" />
                    <ColumnReference Column="Expr1014" />
                    <ColumnReference Column="Expr1018" />
                  </OutputList>
                  <NestedLoops Optimized="0">
                    <RelOp NodeId="2" PhysicalOp="Nested Loops" LogicalOp="Left Outer Join" EstimateRows="25" EstimateIO="0" EstimateCPU="0.0001045" AvgRowSize="129" EstimatedTotalSubtreeCost="0.0192305" Parallel="0" EstimateRebinds="0" EstimateRewinds="0" EstimatedExecutionMode="Row">
                      <OutputList>
                        <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NATIONKEY" />
                        <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                        <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_REGIONKEY" />
                        <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_COMMENT" />
                        <ColumnReference Column="Expr1006" />
                        <ColumnReference Column="Expr1010" />
                        <ColumnReference Column="Expr1014" />
                      </OutputList>
                      <NestedLoops Optimized="0">
                        <RelOp NodeId="3" PhysicalOp="Nested Loops" LogicalOp="Left Outer Join" EstimateRows="25" EstimateIO="0" EstimateCPU="0.0001045" AvgRowSize="126" EstimatedTotalSubtreeCost="0.0139275" Parallel="0" EstimateRebinds="0" EstimateRewinds="0" EstimatedExecutionMode="Row">
                          <OutputList>
                            <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NATIONKEY" />
                            <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                            <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_REGIONKEY" />
                            <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_COMMENT" />
                            <ColumnReference Column="Expr1006" />
                            <ColumnReference Column="Expr1010" />
                          </OutputList>
                          <NestedLoops Optimized="0">
                            <RelOp NodeId="4" PhysicalOp="Nested Loops" LogicalOp="Left Outer Join" EstimateRows="25" EstimateIO="0" EstimateCPU="0.0001045" AvgRowSize="123" EstimatedTotalSubtreeCost="0.0086245" Parallel="0" EstimateRebinds="0" EstimateRewinds="0" EstimatedExecutionMode="Row">
                              <OutputList>
                                <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NATIONKEY" />
                                <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                                <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_REGIONKEY" />
                                <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_COMMENT" />
                                <ColumnReference Column="Expr1006" />
                              </OutputList>
                              <NestedLoops Optimized="0">
                                <RelOp NodeId="5" PhysicalOp="Table Scan" LogicalOp="Table Scan" EstimateRows="25" EstimatedRowsRead="25" EstimateIO="0.003125" EstimateCPU="0.0001845" AvgRowSize="120" EstimatedTotalSubtreeCost="0.0033095" TableCardinality="25" Parallel="0" EstimateRebinds="0" EstimateRewinds="0" EstimatedExecutionMode="Row">
                                  <OutputList>
                                    <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NATIONKEY" />
                                    <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                                    <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_REGIONKEY" />
                                    <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_COMMENT" />
                                  </OutputList>
                                  <TableScan Ordered="0" ForcedIndex="0" ForceScan="0" NoExpandHint="0" Storage="RowStore">
                                    <DefinedValues>
                                      <DefinedValue>
                                        <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NATIONKEY" />
                                      </DefinedValue>
                                      <DefinedValue>
                                        <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                                      </DefinedValue>
                                      <DefinedValue>
                                        <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_REGIONKEY" />
                                      </DefinedValue>
                                      <DefinedValue>
                                        <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_COMMENT" />
                                      </DefinedValue>
                                    </DefinedValues>
                                    <Object Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" TableReferenceId="1" IndexKind="Heap" Storage="RowStore" />
                                    <Predicate>
                                      <ScalarOperator ScalarString="[TPC-H_01].[dbo].[NATION].[N_NAME]=[TPC-H_01].[dbo].[NATION].[N_NAME]">
                                        <Compare CompareOp="EQ">
                                          <ScalarOperator>
                                            <Identifier>
                                              <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                                            </Identifier>
                                          </ScalarOperator>
                                          <ScalarOperator>
                                            <Identifier>
                                              <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                                            </Identifier>
                                          </ScalarOperator>
                                        </Compare>
                                      </ScalarOperator>
                                    </Predicate>
                                  </TableScan>
                                </RelOp>
                                <RelOp NodeId="6" PhysicalOp="Compute Scalar" LogicalOp="Compute Scalar" EstimateRows="1" EstimateIO="0" EstimateCPU="1e-007" AvgRowSize="12" EstimatedTotalSubtreeCost="0.0051985" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                                  <OutputList>
                                    <ColumnReference Column="Expr1006" />
                                  </OutputList>
                                  <ComputeScalar>
                                    <DefinedValues>
                                      <DefinedValue>
                                        <ColumnReference Column="Expr1006" />
                                        <ScalarOperator ScalarString="'%A%'">
                                          <Const ConstValue="'%A%'" />
                                        </ScalarOperator>
                                      </DefinedValue>
                                    </DefinedValues>
                                    <RelOp NodeId="7" PhysicalOp="Top" LogicalOp="Top" EstimateRows="1" EstimateIO="0" EstimateCPU="1e-007" AvgRowSize="9" EstimatedTotalSubtreeCost="0.005196" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                                      <OutputList />
                                      <Top RowCount="0" IsPercent="0" WithTies="0">
                                        <TopExpression>
                                          <ScalarOperator ScalarString="(1)">
                                            <Const ConstValue="(1)" />
                                          </ScalarOperator>
                                        </TopExpression>
                                        <RelOp NodeId="8" PhysicalOp="Table Scan" LogicalOp="Table Scan" EstimateRows="1" EstimatedRowsRead="25" EstimateIO="0.0032035" EstimateCPU="0.000106" AvgRowSize="9" EstimatedTotalSubtreeCost="0.0051935" TableCardinality="25" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                                          <OutputList />
                                          <TableScan Ordered="0" ForcedIndex="0" ForceScan="0" NoExpandHint="0" Storage="RowStore">
                                            <DefinedValues />
                                            <Object Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" TableReferenceId="2" IndexKind="Heap" Storage="RowStore" />
                                          </TableScan>
                                        </RelOp>
                                      </Top>
                                    </RelOp>
                                  </ComputeScalar>
                                </RelOp>
                              </NestedLoops>
                            </RelOp>
                            <RelOp NodeId="9" PhysicalOp="Compute Scalar" LogicalOp="Compute Scalar" EstimateRows="1" EstimateIO="0" EstimateCPU="1e-007" AvgRowSize="12" EstimatedTotalSubtreeCost="0.0051985" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                              <OutputList>
                                <ColumnReference Column="Expr1010" />
                              </OutputList>
                              <ComputeScalar>
                                <DefinedValues>
                                  <DefinedValue>
                                    <ColumnReference Column="Expr1010" />
                                    <ScalarOperator ScalarString="'%A%'">
                                      <Const ConstValue="'%A%'" />
                                    </ScalarOperator>
                                  </DefinedValue>
                                </DefinedValues>
                                <RelOp NodeId="10" PhysicalOp="Top" LogicalOp="Top" EstimateRows="1" EstimateIO="0" EstimateCPU="1e-007" AvgRowSize="9" EstimatedTotalSubtreeCost="0.005196" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                                  <OutputList />
                                  <Top RowCount="0" IsPercent="0" WithTies="0">
                                    <TopExpression>
                                      <ScalarOperator ScalarString="(1)">
                                        <Const ConstValue="(1)" />
                                      </ScalarOperator>
                                    </TopExpression>
                                    <RelOp NodeId="11" PhysicalOp="Table Scan" LogicalOp="Table Scan" EstimateRows="1" EstimatedRowsRead="25" EstimateIO="0.0032035" EstimateCPU="0.000106" AvgRowSize="9" EstimatedTotalSubtreeCost="0.0051935" TableCardinality="25" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                                      <OutputList />
                                      <TableScan Ordered="0" ForcedIndex="0" ForceScan="0" NoExpandHint="0" Storage="RowStore">
                                        <DefinedValues />
                                        <Object Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" TableReferenceId="3" IndexKind="Heap" Storage="RowStore" />
                                      </TableScan>
                                    </RelOp>
                                  </Top>
                                </RelOp>
                              </ComputeScalar>
                            </RelOp>
                          </NestedLoops>
                        </RelOp>
                        <RelOp NodeId="12" PhysicalOp="Compute Scalar" LogicalOp="Compute Scalar" EstimateRows="1" EstimateIO="0" EstimateCPU="1e-007" AvgRowSize="12" EstimatedTotalSubtreeCost="0.0051985" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                          <OutputList>
                            <ColumnReference Column="Expr1014" />
                          </OutputList>
                          <ComputeScalar>
                            <DefinedValues>
                              <DefinedValue>
                                <ColumnReference Column="Expr1014" />
                                <ScalarOperator ScalarString="'%A%'">
                                  <Const ConstValue="'%A%'" />
                                </ScalarOperator>
                              </DefinedValue>
                            </DefinedValues>
                            <RelOp NodeId="13" PhysicalOp="Top" LogicalOp="Top" EstimateRows="1" EstimateIO="0" EstimateCPU="1e-007" AvgRowSize="9" EstimatedTotalSubtreeCost="0.005196" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                              <OutputList />
                              <Top RowCount="0" IsPercent="0" WithTies="0">
                                <TopExpression>
                                  <ScalarOperator ScalarString="(1)">
                                    <Const ConstValue="(1)" />
                                  </ScalarOperator>
                                </TopExpression>
                                <RelOp NodeId="14" PhysicalOp="Table Scan" LogicalOp="Table Scan" EstimateRows="1" EstimatedRowsRead="25" EstimateIO="0.0032035" EstimateCPU="0.000106" AvgRowSize="9" EstimatedTotalSubtreeCost="0.0051935" TableCardinality="25" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                                  <OutputList />
                                  <TableScan Ordered="0" ForcedIndex="0" ForceScan="0" NoExpandHint="0" Storage="RowStore">
                                    <DefinedValues />
                                    <Object Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" TableReferenceId="4" IndexKind="Heap" Storage="RowStore" />
                                  </TableScan>
                                </RelOp>
                              </Top>
                            </RelOp>
                          </ComputeScalar>
                        </RelOp>
                      </NestedLoops>
                    </RelOp>
                    <RelOp NodeId="15" PhysicalOp="Compute Scalar" LogicalOp="Compute Scalar" EstimateRows="1" EstimateIO="0" EstimateCPU="1e-007" AvgRowSize="12" EstimatedTotalSubtreeCost="0.0051985" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                      <OutputList>
                        <ColumnReference Column="Expr1018" />
                      </OutputList>
                      <ComputeScalar>
                        <DefinedValues>
                          <DefinedValue>
                            <ColumnReference Column="Expr1018" />
                            <ScalarOperator ScalarString="'%A%'">
                              <Const ConstValue="'%A%'" />
                            </ScalarOperator>
                          </DefinedValue>
                        </DefinedValues>
                        <RelOp NodeId="16" PhysicalOp="Top" LogicalOp="Top" EstimateRows="1" EstimateIO="0" EstimateCPU="1e-007" AvgRowSize="9" EstimatedTotalSubtreeCost="0.005196" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                          <OutputList />
                          <Top RowCount="0" IsPercent="0" WithTies="0">
                            <TopExpression>
                              <ScalarOperator ScalarString="(1)">
                                <Const ConstValue="(1)" />
                              </ScalarOperator>
                            </TopExpression>
                            <RelOp NodeId="17" PhysicalOp="Table Scan" LogicalOp="Table Scan" EstimateRows="1" EstimatedRowsRead="25" EstimateIO="0.0032035" EstimateCPU="0.000106" AvgRowSize="9" EstimatedTotalSubtreeCost="0.0051935" TableCardinality="25" Parallel="0" EstimateRebinds="0" EstimateRewinds="24" EstimatedExecutionMode="Row">
                              <OutputList />
                              <TableScan Ordered="0" ForcedIndex="0" ForceScan="0" NoExpandHint="0" Storage="RowStore">
                                <DefinedValues />
                                <Object Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" TableReferenceId="5" IndexKind="Heap" Storage="RowStore" />
                              </TableScan>
                            </RelOp>
                          </Top>
                        </RelOp>
                      </ComputeScalar>
                    </RelOp>
                  </NestedLoops>
                </RelOp>
                <Predicate>
                  <ScalarOperator ScalarString="[TPC-H_01].[dbo].[NATION].[N_NAME] like [Expr1006]">
                    <Intrinsic FunctionName="like">
                      <ScalarOperator>
                        <Identifier>
                          <ColumnReference Database="[TPC-H_01]" Schema="[dbo]" Table="[NATION]" Column="N_NAME" />
                        </Identifier>
                      </ScalarOperator>
                      <ScalarOperator>
                        <Identifier>
                          <ColumnReference Column="Expr1006" />
                        </Identifier>
                      </ScalarOperator>
                    </Intrinsic>
                  </ScalarOperator>
                </Predicate>
              </Filter>
            </RelOp>
          </QueryPlan>
        </StmtSimple>
      </Statements>
    </Batch>
  </BatchSequence>
</ShowPlanXML>''')

print("Predicate:")
for predicate in qp.predicates:
    print(predicate)
print("Estimated Rows: " + qp.estimated_rows)
print("Sub Tree Cost: " + qp.estimated_sub_tree_cost)