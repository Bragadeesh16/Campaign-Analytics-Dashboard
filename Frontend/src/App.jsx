import React, { useState, useEffect } from 'react';
import './CompanyDataPage.css';

const CompanyDataPage = () => {
  const [companyData, setCompanyData] = useState([]);
  const [statusFilter, setStatusFilter] = useState('All');

  useEffect(() => {
    fetch('http://localhost:5000/dashboard')
      .then((res) => res.json())
      .then((data) => setCompanyData(data))
      .catch((err) => console.error('Error fetching data:', err));
  }, []);

  const filteredData =
    statusFilter === 'All'
      ? companyData
      : companyData.filter((item) => item.Status === statusFilter);

  console.log('Filtered Data:', filteredData);

  return (
    <div className="container">
      <h1>Company Lists</h1>

      <div className="filter">
        <label htmlFor="statusFilter">Filter by status: </label>
        <select
          id="statusFilter"
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
        >
          <option value="All">All</option>
          <option value="active">active</option>
          <option value="paused">paused</option>
        </select>
      </div>

      <table>
        <thead>
          <tr>
            <th>Campaign Name</th>
            <th>Status</th>
            <th>Clicks</th>
            <th>Cost</th>
            <th>Impressions</th>
          </tr>
        </thead>
        <tbody>
          
          {filteredData.map((campaign, index) => (
            <tr key={index}>
              <td>{campaign.Company_name}</td>
              <td>{campaign.Status}</td>
              <td>{campaign.Clicks}</td>
              <td>${campaign.Cost}</td>
              <td>{campaign.Impressions}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p> {filteredData.Status} </p>
    </div>
  );
};

export default CompanyDataPage;
